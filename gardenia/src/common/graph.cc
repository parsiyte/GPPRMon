#include "graph.hh"
#include "scan.h"

Graph::Graph(std::string prefix, bool use_dag, bool has_vlabel) :
    vlabels(NULL), elabels(NULL), nnz(0) {
  VertexSet::release_buffers();
  std::ifstream f_meta((prefix + ".meta.txt").c_str());
  assert(f_meta);
  int vid_size;
  f_meta >> n_vertices >> n_edges >> vid_size >> max_degree;
  assert(sizeof(vidType) == vid_size);
  f_meta.close();
  // read row pointers
  if (map_vertices) map_file(prefix + ".vertex.bin", vertices, n_vertices+1);
  else read_file(prefix + ".vertex.bin", vertices, n_vertices+1);
  // read column indices
  if (map_edges) map_file(prefix + ".edge.bin", edges, n_edges);
  else read_file(prefix + ".edge.bin", edges, n_edges);
  num_vertex_classes = 0;
  // read vertex labels
  if (has_vlabel) {
    std::string vlabel_filename = prefix + ".vlabel.bin";
    ifstream f_vlabel(vlabel_filename.c_str());
    if (f_vlabel.good()) {
      if (map_vlabels) map_file(vlabel_filename, vlabels, n_vertices);
      else read_file(vlabel_filename, vlabels, n_vertices);
      std::set<vlabel_t> labels;
      for (vidType v = 0; v < n_vertices; v++)
        labels.insert(vlabels[v]);
      num_vertex_classes = labels.size();
    } else {
      std::cout << "WARNING: vertex label file not exist; generating random labels\n";
      num_vertex_classes = 4;
      vlabels = new vlabel_t[n_vertices];
      for (vidType v = 0; v < n_vertices; v++) {
        vlabels[v] = rand() % num_vertex_classes + 1;
      }
    }
  }
  if (max_degree == 0 || max_degree>=n_vertices) exit(1);
  if (use_dag) orientation();
  VertexSet::MAX_DEGREE = std::max(max_degree, VertexSet::MAX_DEGREE);
  labels_frequency_.clear();
}

Graph::~Graph() {
  if (map_edges) munmap(edges, n_edges*sizeof(vidType));
  else custom_free(edges, n_edges);
  if (map_vertices) {
    munmap(vertices, (n_vertices+1)*sizeof(eidType));
  } else custom_free(vertices, n_vertices+1);
  if (vlabels != NULL) delete [] vlabels;
}

VertexSet Graph::N(vidType vid) const {
  assert(vid >= 0);
  assert(vid < n_vertices);
  eidType begin = vertices[vid], end = vertices[vid+1];
  if (begin > end) {
    fprintf(stderr, "vertex %u bounds error: [%lu, %lu)\n", vid, begin, end);
    exit(1);
  }
  assert(end <= n_edges);
  return VertexSet(edges + begin, end - begin, vid);
}

void Graph::orientation() {
  std::cout << "Orientation enabled, using DAG\n";
  Timer t;
  t.Start();
  std::vector<vidType> degrees(n_vertices, 0);
  #pragma omp parallel for
  for (vidType v = 0; v < n_vertices; v++) {
    degrees[v] = get_degree(v);
  }
  std::vector<vidType> new_degrees(n_vertices, 0);
  #pragma omp parallel for
  for (vidType src = 0; src < n_vertices; src ++) {
    for (auto dst : N(src)) {
      if (degrees[dst] > degrees[src] ||
          (degrees[dst] == degrees[src] && dst > src)) {
        new_degrees[src]++;
      }
    }
  }
  max_degree = *(std::max_element(new_degrees.begin(), new_degrees.end()));
  eidType *old_vertices = vertices;
  vidType *old_edges = edges;
  eidType *new_vertices = custom_alloc_global<eidType>(n_vertices+1);
  //prefix_sum<vidType,eidType>(new_degrees, new_vertices);
  parallel_prefix_sum<vidType,eidType>(new_degrees, new_vertices);
  auto num_edges = new_vertices[n_vertices];
  vidType *new_edges = custom_alloc_global<vidType>(num_edges);
  #pragma omp parallel for
  for (vidType src = 0; src < n_vertices; src ++) {
    auto begin = new_vertices[src];
    eidType offset = 0;
    for (auto dst : N(src)) {
      if (degrees[dst] > degrees[src] ||
          (degrees[dst] == degrees[src] && dst > src)) {
        new_edges[begin+offset] = dst;
        offset ++;
      }
    }
  }
  vertices = new_vertices;
  edges = new_edges;
  custom_free<eidType>(old_vertices, n_vertices);
  custom_free<vidType>(old_edges, n_edges);
  n_edges = num_edges;
  t.Stop();
  std::cout << "Time on generating the DAG: " << t.Seconds() << " sec\n";
}

void Graph::print_graph() const {
  std::cout << "Printing the graph: \n";
  for (vidType n = 0; n < n_vertices; n++) {
    std::cout << "vertex " << n << ": degree = " 
      << get_degree(n) << " edgelist = [ ";
    for (auto e = edge_begin(n); e != edge_end(n); e++)
      std::cout << getEdgeDst(e) << " ";
    std::cout << "]\n";
  }
}

eidType Graph::init_edgelist(bool sym_break, bool ascend) {
  Timer t;
  t.Start();
  if (nnz != 0) return nnz; // already initialized
  nnz = E();
  if (sym_break) nnz = nnz/2;
  sizes.resize(V());
  src_list = new vidType[nnz];
  if (sym_break) dst_list = new vidType[nnz];
  else dst_list = edges;
  size_t i = 0;
  for (vidType v = 0; v < V(); v ++) {
    for (auto u : N(v)) {
      if (u == v) continue; // no selfloops
      if (ascend) {
        if (sym_break && v > u) continue;  
      } else {
        if (sym_break && v < u) break;  
      }
      src_list[i] = v;
      if (sym_break) dst_list[i] = u;
      sizes[v] ++;
      i ++;
    }
  }
  //assert(i == nnz);
  t.Stop();
  std::cout << "Time on generating the edgelist: " << t.Seconds() << " sec\n";
  return nnz;
}

bool Graph::is_connected(vidType v, vidType u) const {
  auto v_deg = get_degree(v);
  auto u_deg = get_degree(u);
  bool found;
  if (v_deg < u_deg) {
    found = binary_search(u, edge_begin(v), edge_end(v));
  } else {
    found = binary_search(v, edge_begin(u), edge_end(u));
  }
  return found;
}

bool Graph::is_connected(std::vector<vidType> sg) const {
  return false;
}

bool Graph::binary_search(vidType key, eidType begin, eidType end) const {
  auto l = begin;
  auto r = end-1;
  while (r >= l) { 
    auto mid = l + (r - l) / 2;
    auto value = getEdgeDst(mid);
    if (value == key) return true;
    if (value < key) l = mid + 1; 
    else r = mid - 1; 
  } 
  return false;
}

vidType Graph::intersect_num(vidType v, vidType u) {
  vidType num = 0;
  vidType idx_l = 0, idx_r = 0;
  vidType v_size = get_degree(v);
  vidType u_size = get_degree(u);
  vidType* v_ptr = &edges[vertices[v]];
  vidType* u_ptr = &edges[vertices[u]];
  while (idx_l < v_size && idx_r < u_size) {
    vidType a = v_ptr[idx_l];
    vidType b = u_ptr[idx_r];
    if (a <= b) idx_l++;
    if (b <= a) idx_r++;
    if (a == b) num++;
  }
  return num;
}

vidType Graph::intersect_num(vidType v, vidType u, vlabel_t label) {
  vidType num = 0;
  vidType idx_l = 0, idx_r = 0;
  vidType v_size = get_degree(v);
  vidType u_size = get_degree(u);
  vidType* v_ptr = &edges[vertices[v]];
  vidType* u_ptr = &edges[vertices[u]];
  while (idx_l < v_size && idx_r < u_size) {
    vidType a = v_ptr[idx_l];
    vidType b = u_ptr[idx_r];
    if (a <= b) idx_l++;
    if (b <= a) idx_r++;
    if (a == b && vlabels[a] == label) num++;
  }
  return num;
}

void Graph::BuildReverseIndex() {
  if (labels_frequency_.empty()) computeLabelsFrequency();
  int nl = num_vertex_classes;
  if (max_label == num_vertex_classes) nl += 1;
  reverse_index_.resize(size());
  reverse_index_offsets_.resize(nl+1);
  reverse_index_offsets_[0] = 0;
  vidType total = 0;
  for (int i = 0; i < nl; ++i) {
    total += labels_frequency_[i];
    reverse_index_offsets_[i+1] = total;
    //std::cout << "label " << i << " frequency: " << labels_frequency_[i] << "\n";
  }
  std::vector<eidType> start(nl);
  for (int i = 0; i < nl; ++i) {
    start[i] = reverse_index_offsets_[i];
    //std::cout << "label " << i << " start: " << start[i] << "\n";
  }
  for (vidType i = 0; i < size(); ++i) {
    auto vl = vlabels[i];
    reverse_index_[start[vl]++] = i;
  }
}

#pragma omp declare reduction(vec_plus : std::vector<int> : \
    std::transform(omp_out.begin(), omp_out.end(), omp_in.begin(), omp_out.begin(), std::plus<int>())) \
    initializer(omp_priv = decltype(omp_orig)(omp_orig.size()))
void Graph::computeLabelsFrequency() {
  labels_frequency_.resize(num_vertex_classes+1);
  std::fill(labels_frequency_.begin(), labels_frequency_.end(), 0);
  //max_label = int(*std::max_element(vlabels, vlabels+size()));
  #pragma omp parallel for reduction(max:max_label)
  for (int i = 0; i < size(); ++i) {
    max_label = max_label > vlabels[i] ? max_label : vlabels[i];
  }
  #pragma omp parallel for reduction(vec_plus:labels_frequency_)
  for (vidType v = 0; v < size(); ++v) {
    int label = int(get_vlabel(v));
    assert(label <= num_vertex_classes);
    labels_frequency_[label] += 1;
  }
  max_label_frequency_ = int(*std::max_element(labels_frequency_.begin(), labels_frequency_.end()));
  //std::cout << "max_label = " << max_label << "\n";
  //std::cout << "max_label_frequency_ = " << max_label_frequency_ << "\n";
  //for (size_t i = 0; i < labels_frequency_.size(); ++i)
  //  std::cout << "label " << i << " vertex frequency: " << labels_frequency_[i] << "\n";
}

int Graph::get_frequent_labels(int threshold) {
  int num = 0;
  for (size_t i = 0; i < labels_frequency_.size(); ++i)
    if (labels_frequency_[i] > threshold)
      num++;
  return num;
}

bool Graph::is_freq_vertex(vidType v, int threshold) {
  assert(v >= 0 && v < size());
  auto label = int(vlabels[v]);
  assert(label <= num_vertex_classes);
  if (labels_frequency_[label] >= threshold) return true;
  return false;
}

void Graph::BuildNLF() {
  //std::cout << "Building NLF map for the data graph\n";
  nlf_.resize(size());
  #pragma omp parallel for
  for (vidType v = 0; v < size(); ++v) {
    for (auto u : N(v)) {
      auto vl = get_vlabel(u);
      if (nlf_[v].find(vl) == nlf_[v].end())
        nlf_[v][vl] = 0;
      nlf_[v][vl] += 1;
    }
  }
}

void Graph::print_meta_data() const {
  std::cout << "|V|: " << n_vertices << ", |E|: " << n_edges << ", Max Degree: " << max_degree << "\n";
  if (num_vertex_classes > 0) {
    std::cout << "|\u03A3|: " << num_vertex_classes
              << ", Max Label Frequency: " << max_label_frequency_ << "\n";
  }
}


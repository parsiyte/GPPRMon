#pragma once
#include <set>

inline unsigned bounded_intersect_merge(Graph& graph, unsigned p, unsigned q, int bound) {
  unsigned count = 0;
  auto p_start   = graph.edge_begin(p);
  auto p_end     = graph.edge_end(p);
  auto q_start   = graph.edge_begin(q);
  auto q_end     = graph.edge_end(q);
  auto p_it      = p_start;
  auto q_it      = q_start;
  int a;
  int b;
  while (p_it < p_end && q_it < q_end) {
    a = (int)graph.getEdgeDst(p_it);
    b = (int)graph.getEdgeDst(q_it);
    if (a >= bound || b >= bound) break;
    int d = a - b;
    if (d <= 0) p_it++;
    if (d >= 0) q_it++;
    if (d == 0) count++;
  }
  return count;
}

inline unsigned intersect_merge(Graph& graph, unsigned p, unsigned q) {
  unsigned count = 0;
  auto p_start   = graph.edge_begin(p);
  auto p_end     = graph.edge_end(p);
  auto q_start   = graph.edge_begin(q);
  auto q_end     = graph.edge_end(q);
  auto p_it      = p_start;
  auto q_it      = q_start;
  int a;
  int b;
  while (p_it < p_end && q_it < q_end) {
    a = (int)graph.getEdgeDst(p_it);
    b = (int)graph.getEdgeDst(q_it);
    int d = a - b;
    if (d <= 0) p_it++;
    if (d >= 0) q_it++;
    if (d == 0) count++;
  }
  return count;
}

inline unsigned bounded_intersect_merge_except(Graph& graph, unsigned p, unsigned q, int bound, std::set<int> vset) {
  unsigned count = 0;
  auto p_start   = graph.edge_begin(p);
  auto p_end     = graph.edge_end(p);
  auto q_start   = graph.edge_begin(q);
  auto q_end     = graph.edge_end(q);
  auto p_it      = p_start;
  auto q_it      = q_start;
  int a;
  int b;
  while (p_it < p_end && q_it < q_end) {
    a = (int)graph.getEdgeDst(p_it);
    b = (int)graph.getEdgeDst(q_it);
    if (a >= bound || b >= bound) break;
    int d = a - b;
    if (d <= 0) p_it++;
    if (d >= 0) q_it++;
    if (d == 0 && vset.find(a) == vset.end())
      count++;
  }
  return count;
}

inline unsigned intersect(Graph& graph, unsigned p, unsigned q) {
  return intersect_merge(graph, p, q);
}

inline unsigned bounded_intersect(Graph& graph, unsigned p, unsigned q, unsigned bound) {
  return bounded_intersect_merge(graph, p, q, int(bound));
}

inline unsigned bounded_intersect_except(Graph& graph, unsigned p, unsigned q, unsigned bound, unsigned r) {
  std::set<int> vertex_set;
  vertex_set.insert(int(r));
  return bounded_intersect_merge_except(graph, p, q, int(bound), vertex_set);
}


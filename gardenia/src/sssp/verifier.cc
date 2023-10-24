// Copyright 2020 MIT
// Authors: Xuhao Chen <cxh@mit.edu>
#include <queue>
#include <iostream>
#include "sssp.h"
#include "timer.h"

void SSSPVerifier(Graph &g, int source, DistT *weight, DistT *dist_to_test) {
	printf("Verifying...\n");
	// Serial Dijkstra implementation to get oracle distances
	vector<DistT> oracle_dist(g.V(), kDistInf);
	typedef pair<DistT, IndexT> WN;
	priority_queue<WN, vector<WN>, greater<WN> > mq;
	int iter = 0;
	Timer t;
	t.Start();
	oracle_dist[source] = 0;
	mq.push(make_pair(0, source));
	while (!mq.empty()) 
	{
		DistT td = mq.top().first;
		IndexT src = mq.top().second;
		mq.pop();
		if (td == oracle_dist[src]) {
      auto offset = g.edge_begin(src);
      for (auto dst : g.N(src)) {
				DistT wt = weight[offset++];
				if (td + wt < oracle_dist[dst]) {
					oracle_dist[dst] = td + wt;
					mq.push(make_pair(td + wt, dst));
				}
			}
		}
		iter ++;
	}
	t.Stop();
	printf("\titerations = %d.\n", iter);
	printf("\truntime [verify] = %f ms.\n", t.Millisecs());

	// Report any mismatches
	unsigned err = 0;
	unsigned err_1 = 0;
	unsigned err_2 = 0;
	unsigned err_3 = 0;
	unsigned err_4 = 0;

	float errPercent = 0;
	bool all_ok = true;
	for (int n = 0; n < g.V(); n ++) {
		if (dist_to_test[n] != oracle_dist[n]) 
		{
			err++;
			int res = dist_to_test[n] - oracle_dist[n];
			errPercent = ((float)res / dist_to_test[n]) * 100;

			if (errPercent <= 1)
				err_1++;
			else if (errPercent > 1 && errPercent <= 5)
				err_2++;
			else if (errPercent > 5 && errPercent <= 10)
				err_3++;
			else
				err_4++;
			all_ok = false;
		}
	}

	printf("Total element = %d, || elements whose err <= %1 = %d || elements whose %1 < err <= %5 = %d"
				 " || elements whose %5 < err <= %10 = %d || elements whose %10 < err = %d || total err Element = %d\n",
				 g.V(), err_1, err_2, err_3, err_4, err);

	if(all_ok) 
		printf("Correct\n");
	else 
		printf("Wrong\n");
}


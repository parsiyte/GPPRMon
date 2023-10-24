// Copyright 2020 MIT
// Authors: Xuhao Chen <cxh@mit.edu>
#include <iostream>
#include <vector>
#include "bfs.h"
#include "timer.h"

void BFSVerifier(Graph &g, int source, DistT *depth_to_test) 
{
	std::cout << "Verifying...\n";
  auto m = g.V();
	vector<DistT> depth(m, MYINFINITY);
	vector<int> to_visit;
	Timer t;
	t.Start();
	depth[source] = 0;
	to_visit.reserve(m);
	to_visit.push_back(source);
	for (std::vector<int>::iterator it = to_visit.begin(); it != to_visit.end(); it++) 
	{
		int src = *it;
    for (auto dst : g.N(src)) 
		{
			if (depth[dst] == MYINFINITY) {
				depth[dst] = depth[src] + 1;
				to_visit.push_back(dst);
			}
		}
	}
	t.Stop();
	printf("\truntime [serial] = %f ms.\n", t.Millisecs());

	// Report any mismatches
	unsigned err = 0;
	unsigned err_1 = 0;
	unsigned err_2 = 0;
	unsigned err_3 = 0;
	unsigned err_4 = 0;
	unsigned err_5 = 0;
	float errPercent = 0;

	bool all_ok = true;
	for (int n = 0; n < m; n ++) {
		if (depth_to_test[n] != depth[n]) 
		{			
			err++;
			double res = std::abs(depth_to_test[n] != depth[n]);
			errPercent = (res / std::abs(depth_to_test[n])) * 100;
			if (errPercent <= 0.1)
				err_1++;
			else if (errPercent > 0.1 && errPercent <= 1)
				err_2++;
			else if (errPercent > 1 && errPercent <= 5)
				err_3++;
			else if (errPercent > 5 && errPercent <= 10)
				err_4++;
			else
				err_5++;
			//std::cout << n << ": " << depth_to_test[n] << " != " << depth[n] << std::endl;
			all_ok = false;
		}
	}
	printf("Total element = %u, || elements whose err <= %0.1 = %d || elements whose 0.1 < err  <= %1 = %d || elements whose %1 < err <= %5 = %d"
				 " || elements whose %5 < err <= %10 = %d || elements whose %10 < err = %d || total err Element = %d\n",
				 m, err_1, err_2, err_3, err_4, err_5, err);
	if(all_ok) 
		printf("Correct\n");
	else 
		printf("Wrong\n");
}


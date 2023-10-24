// Copyright 2020 MIT
// Authors: Xuhao Chen <cxh@mit.edu>
// Verifies by asserting a single serial iteration in push direction has
//   error < target_error
#include "pr.h"
#include "timer.h"

void PRVerifier(Graph &g, ScoreT *scores_to_test, double target_error) 
{
	std::cout << "Verifying...\n";
  auto m = g.V();
	const ScoreT base_score = (1.0f - kDamp) / m;
	const ScoreT init_score = 1.0f / m;
	ScoreT *scores = (ScoreT *) malloc(m * sizeof(ScoreT));
	for (int i = 0; i < m; i ++) scores[i] = init_score;
	ScoreT *outgoing_contrib = (ScoreT *) malloc(m * sizeof(ScoreT));
	//for (int i = 0; i < m; i ++) outgoing_contrib[i] = 0;
	int iter;
	Timer t;
	t.Start();
	for (iter = 0; iter < MAX_ITER; iter ++) 
	{
		double error = 0;
		for (int n = 0; n < m; n ++)
			outgoing_contrib[n] = scores[n] / g.get_degree(n);
		for (int src = 0; src < m; src ++) {
			ScoreT incoming_total = 0;
      for (auto dst : g.in_neigh(src)) 
				incoming_total += outgoing_contrib[dst];
			ScoreT old_score = scores[src];
			scores[src] = base_score + kDamp * incoming_total;
			error += fabs(scores[src] - old_score);
		}   
		printf(" %2d    %lf\n", iter+1, error);
		if (error < EPSILON) 
			break;
	}
	t.Stop();
	if (iter < MAX_ITER) iter ++;
	printf("\titerations = %d.\n", iter);
	printf("\truntime [serial] = %f ms.\n", t.Millisecs());
	
	ScoreT *incomming_sums = (ScoreT *)malloc(m * sizeof(ScoreT));

	for(int i = 0; i < m; i ++) 
		incomming_sums[i] = 0;

	double error = 0;
	for (int src = 0; src < m; src ++) 
	{
		ScoreT outgoing_contrib = scores_to_test[src] / g.get_degree(src);
    for (auto dst : g.out_neigh(src)) 
			incomming_sums[dst] += outgoing_contrib;
	}

	unsigned err = 0;
	unsigned err_1 = 0;
	unsigned err_2 = 0;
	unsigned err_3 = 0;
	unsigned err_4 = 0;
	unsigned err_5 = 0;
	unsigned tot = 0; 
	double errPercent = 0;

	for (int i = 0; i < m; i ++) 
	{
		ScoreT new_score = base_score + kDamp * incomming_sums[i];

		error += fabs(new_score - scores_to_test[i]);

		float res = fabs(new_score - scores_to_test[i]);
//		if (res == (double)0) {
//			printf("res = %lf, new_score = %lf, scores_to_test[%d] = %lf\n", 
//						  res, new_score, i, scores_to_test[i]);
//		}
									// 0.01 / 0.001
		errPercent = (res / fabs(scores_to_test[i])) * 100;
		if (errPercent <= 0.1)
			err_1++;
		else if (errPercent > 0.1 && errPercent <= 1)
			err_2++;
		else if (errPercent > 1 && errPercent <= 5)
			err_3++;
		else if (errPercent > 5 && errPercent <= 10)
			err_4++;
		else if (errPercent > 100)
			err_5++;
		incomming_sums[i] = 0;
	}
	printf("Total element = %d, || elements whose err <= %0.1 = %d "
	       "|| elements whose 0.1 < err  <= %1 = %d || elements whose %1 < err <= %5 = %d"
				 " || elements whose %5 < err <= %10 = %d || elements whose %10 < err = %d ||"
				 " total err Element = %lf\n",
				 m, err_1, err_2, err_3, err_4, err_5, error);

	if (error < target_error) 
		printf("Correct\n");
	else 
		printf("Total Error: %f\n", error);
}


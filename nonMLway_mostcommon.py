import sys
import csv
import os
import numpy as np
import pandas as pd
import ml_metrics as metrics

test_data = "../Data/test.csv"
train_data = "../Data/train.csv"
client_data = "../Data/cliente_tabla.csv"
product_data = "../Data/producto_tabla.csv"
depot_data = "../Data/town_state.csv"
sample_data = "../Data/sample_submission.csv"

#test = pd.read_csv(test_data)
train = pd.read_csv(train_data, usecols=['Demanda_uni_equil'])
#client = pd.read_csv(client_data)
#product = pd.read_csv(product_data)
#depot = pd.read_csv(depot_data)
"""
bestscore = 100
best_value = -1

for i in range(12):
	train['pred'] = i
	score = metrics.rmsle(train['pred'].tolist(),train['Demanda_uni_equil'].tolist())
	print "i is %d, score is %s"%(i,score)
	if score<bestscore:
		bestscore = score
		best_value = i
"""
"""
i is 0, score is 1.80674216009
i is 1, score is 1.23396170879
i is 2, score is 0.9743239479
i is 3, score is 0.861343016654
i is 4, score is 0.833685129237
i is 5, score is 0.854781517127
i is 6, score is 0.901463038437
i is 7, score is 0.96024377829
i is 8, score is 1.02381394769
i is 9, score is 1.08836109037
i is 10, score is 1.1519486572
i is 11, score is 1.21363163951
"""

best_value = 4
min_float = best_value - 0.9
max_float = best_value + 0.9
best_value = -1
bestscore = 100

for i in np.arange(min_float,max_float,0.1).tolist():
	train['pred'] = i
	score = metrics.rmsle(train['pred'].tolist(),train['Demanda_uni_equil'].tolist())
	print "i is %f, score is %s"%(i,score)
	if score<bestscore:
		bestscore = score
		best_value = i

sub = pd.read_csv(sample_data)
sub['Demanda_uni_equil'] = best_value
sub.to_csv('Naive_submission_mostcommon.csv', index=False)

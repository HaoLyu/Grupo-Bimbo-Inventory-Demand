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
#train = pd.read_csv(train_data, usecols=['Demanda_uni_equil'])
#client = pd.read_csv(client_data)
#product = pd.read_csv(product_data)
#depot = pd.read_csv(depot_data)

#sub = pd.read_csv(sample_data)
#sub['Demanda_uni_equil'] = best_value
#sub.to_csv('Naive_submission_mostcommon.csv', index=False)

f = open(train_data, "r")
f.readline()

latest_demand_clpro = dict()
global_median = list()
agencia_product = {}
total = 0

while 1:

	line = f.readline().strip()
	total += 1

	if total % 5000000 == 0:
		print('Read {} lines...'.format(total))

	if line == '':
		break

	arr = line.split(",")

	semana = int(arr[0])
	agencia = int(arr[1])
	canal = int(arr[2])
	ruta = int(arr[3])
	cliente = int(arr[4])
	producto = int(arr[5])
	demanda = int(arr[10])

	if agencia != '' and producto != '':
		ap = (agencia, producto)
		if ap not in agencia_product:
			agencia_product[ap] = [demanda]
		else:
			agencia_product[ap].append(demanda)

	if cliente != '' and producto != '':
		hsh = (agencia, cliente, producto)
		if hsh in latest_demand_clpro:
			latest_demand_clpro[hsh] = ((.5 * latest_demand_clpro[hsh]) + (.5 * demanda))
		else:
			latest_demand_clpro[hsh] = demanda

	list.append(global_median, demanda)

f.close()

for key in agencia_product:
	agencia_product[key] = np.mean(agencia_product[key])

print ('')
path = ('submission.csv')
out = open(path, "w")
f = open(test_data, "r")
f.readline()

out.write("id,Demanda_uni_equil\n")
median_demanda = np.median(global_median)

total = 0
total1 = 0
total2 = 0
total3 = 0
while 1:

	line = f.readline().strip()
	total += 1

	if total % 1000000 == 0:
		print('Write {} lines...'.format(total))

	if line == '':
		break

	arr = line.split(",")

	id = int(arr[0])
	semana = int(arr[1])
	agencia = int(arr[2])
	cliente = int(arr[5])
	producto = int(arr[6])

	out.write(str(id) + ',')

	hsh = (agencia, cliente, producto)
	ap = (agencia, producto)
	if hsh in latest_demand_clpro:
		d = latest_demand_clpro[hsh]
		out.write(str(d))
		total1 += 1
	elif ap in agencia_product:
		d = agencia_product[ap]
		out.write(str(d))
		total3 += 1
	else:
		out.write(str(round(median_demanda)))
		total2 += 1

	out.write("\n")
out.close()

print ('')

print ('Total 1: {} ...'.format(total1))
print ('Total 2: {} ...'.format(total2))
print ('Total 2: {} ...'.format(total3))
print ('')
print ('Completed!')
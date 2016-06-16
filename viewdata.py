import sys
import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_data = "./Data/test.csv"
train_data = "./Data/train.csv"
client_data = "./Data/cliente_tabla.csv"
product_data = "./Data/producto_tabla.csv"
depot_data = "./Data/town_state.csv"

test = pd.read_csv(test_data)
train = pd.read_csv(train_data)
client = pd.read_csv(client_data)
product = pd.read_csv(product_data)
depot = pd.read_csv(depot_data)

print "test fields: \n", test.columns.values, "\nshape", test.shape
print "train fields: \n", train.columns.values, "\nshape", train.shape
print "client fields: \n", client.columns.values, "\nshape", client.shape
print "product fields: \n", product.columns.values, "\nshape", product.shape
print "depot fields: \n", depot.columns.values, "\nshape", depot.shape

"""
test fields:
['id' 'Semana' 'Agencia_ID' 'Canal_ID' 'Ruta_SAK' 'Cliente_ID'
 'Producto_ID'] 
shape (6999251, 7)
train fields: 
['Semana' 'Agencia_ID' 'Canal_ID' 'Ruta_SAK' 'Cliente_ID' 'Producto_ID'
 'Venta_uni_hoy' 'Venta_hoy' 'Dev_uni_proxima' 'Dev_proxima'
 'Demanda_uni_equil'] 
shape (74180464, 11)
client fields: 
['Cliente_ID' 'NombreCliente'] 
shape (935362, 2)
product fields: 
['Producto_ID' 'NombreProducto'] 
shape (2592, 2)
depot fields: 
['Agencia_ID' 'Town' 'State'] 
shape (790, 3)

Semana — Week number (From Thursday to Wednesday)
Agencia_ID — Sales Depot ID
Canal_ID — Sales Channel ID
Ruta_SAK — Route ID (Several routes = Sales Depot)
Cliente_ID — Client ID
NombreCliente — Client name
Producto_ID — Product ID
NombreProducto — Product Name
Venta_uni_hoy — Sales unit this week (integer)
Venta_hoy — Sales this week (unit: pesos)
Dev_uni_proxima — Returns unit next week (integer)
Dev_proxima — Returns next week (unit: pesos)
Demanda_uni_equil — Adjusted Demand (integer) (This is the target you will predict)

"""

print test.describe()
print len(test.Canal_ID.unique()), len(test.Semana.unique()), len(test.Agencia_ID.unique())
print len(test.Ruta_SAK.unique()), len(test.Cliente_ID.unique()), len(test.Producto_ID.unique())
"""
9, 2, 552
2608, 745164, 1522
"""
print "#"*20

print train.describe()
print len(train.Canal_ID.unique()), len(train.Semana.unique()), len(train.Agencia_ID.unique())
print len(train.Ruta_SAK.unique()), len(train.Cliente_ID.unique()), len(train.Producto_ID.unique())
"""
9, 7, 552
3603, 880604, 1799
"""
print "#"*20

def label_plot(title, x, y):
	plt.title(title)
	plt.xlabel(x)
	plt.ylabel(y)

target = df_train['Demanda_uni_equil'].tolist()
plt.hist(target, bins=50, color='blue', range=(0, 50))
label_plot('Distribution of target values under 50', 'Demanda_uni_equil', 'Count')
plt.show()

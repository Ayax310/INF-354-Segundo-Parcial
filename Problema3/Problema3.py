# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:03:35 2020

@author: Ayax
"""
import pandas as pd
import numpy as np

datos = pd.read_csv('crx.data', sep=',',header=None)
datos = datos.replace(np.nan, '0')
datos = datos.replace('?', '10')

print(datos)

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
datos['columna1']=encoder.fit_transform(datos[1].values)
arreglo = np.array(datos[4])
datos[4] = np.where(arreglo == '10', 'g', arreglo)
datos['columna4']=encoder.fit_transform(datos[4].values)
datos['columna12']=encoder.fit_transform(datos[12].values)
#print(datos.columna1.unique())
#print(datos.columna4.unique())
#print(datos.columna12.unique())

#Datos de entrada
X=datos[['columna1','columna4','columna12']]
#X=datos[['columna1','columna4']]
#X=datos['columna1']
#print(X)

#Datos de salida
y=datos['columna12']
#y=datos['columna4']
#print(y)

#Cuantos datos se necesitan para entrenamiento y cuantos para prueba 80-20
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Red neuronal
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, alpha=1e-5, solver='lbfgs', random_state=300,tol=1e-2)
#Entrenamiento
mlp.fit(X_train,y_train)
predictions=mlp.predict(X_test)

from sklearn.metrics import confusion_matrix
matriz = confusion_matrix(y_test, predictions)
print(matriz)

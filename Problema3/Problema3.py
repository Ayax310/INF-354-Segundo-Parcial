# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:03:35 2020

@author: Ayax
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
seed = 100

# cargamos el dataset
datos = pd.read_csv("crx.data", header=None)

# Viendo los datos 
print(datos)
print("\n")

# sacamos las estadisticas de los datos numericos
print('*************Estadisticas************')
datos_descr = datos.describe()
print(datos_descr)

print("\n")

# viendo los valores faltantes

import numpy as np

print('*************Numero de NUlls************')
# vemos y contammos los datos en null
print(datos.isnull().values.sum())

# Remplazamos los valores '?' con NaN
datos = datos.replace("?",np.NaN)

# Imputamos los valores NAN con la media
datos = datos.fillna(datos.mean())

print('*************Numero de NUlls 2************')
# contamos le numero de NUll de nuevo para verificar
print(datos.isnull().values.sum())

# En todas las columnas e imputamos los valores NAN 

for col in datos.columns:
    #vemos si es de tipo object - nominal
    if datos[col].dtypes == 'object':
        # imputamos con la moda
        datos[col] = datos[col].fillna(datos[col].value_counts().index[0])

# y finalmente contamos otra vez los valores NAN 
print('*************Numero de NUlls 3************')
print(datos.isnull().values.sum())

print("\n")
print('*************Preprocesamiento 1************')

#Categorizamos
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
# con todas las tablas cambiamos las valores no numericos a numericos en un rango 
for col in datos.columns:
    #vemos si es de tipo object - nominal
    if datos[col].dtype=='object':
    # tanfomramos los valores no numericos
        datos[col]=le.fit_transform(datos[col])
        
print(datos)      
       

print("\n")
print('*************Preprocesamiento 2************')
# Normalizamos con minmaxscaler

from sklearn.preprocessing import MinMaxScaler

# Elimina los campos 10 y 13 y convierta el DataFrame en una matriz NumPy
datos = datos.drop([datos.columns[10],datos.columns[13]], axis=1)

print(datos)

datos = datos.values

# Separa los campos y etiquetas en variables separadas
X,y = datos[:,0:13], datos[:,13]

#  instanciamos  MinMaxScaler y reescalonamos
esc = MinMaxScaler(feature_range=(0,1))
rescX = esc.fit_transform(X)

print('*************Seleccion Entrenamiento 80% y Test 20%************')
# Entrenaminto y Test
from sklearn.model_selection import train_test_split

# dividimos en test y entrenamietno 
Xtrain, Xtest, ytrain, ytest = train_test_split(rescX,
                                                    y,
        
                                                    test_size=0.20,
                                                    random_state=42)
print('*********Tamaños**********')
print("Train: ", len(Xtrain))
print("Test: ", len(Xtest))

print('*********** Red Neuronal Clasificador Multilayer Perceptron************')
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,  hidden_layer_sizes=(5, 2), random_state=300)
clf.fit(Xtrain, ytrain)
Ypred = clf.predict(Xtest)

print('********TEST********')
print(ytest)
print('*******PREDICT******')
print(Ypred)
print()
print('*************Matriz de confusion***********')
print(confusion_matrix(ytest, Ypred))
print("Exactitud: ", accuracy_score(ytest, Ypred)*100)
        

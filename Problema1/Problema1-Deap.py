# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:33:43 2020

@author: Ayax
"""
import random
import array
import numpy
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
#Definimos la matriz al leer desde un archivo csv
matriz = pd.read_csv("Ejercicio1.csv", sep=',',header=None)
#Mostramos la matriz
print (matriz.values)
#Definimos el tamaño del indice
NB_QUEENS = 4

caminos = matriz
#Calculo de la distancia que recorre el viajero
#Función objetivo
def evalPAV(individual): 
    #Ruta entre el último y el primero 
    ruta = caminos[individual[-1]][individual[0]]
    #Ruta entre las demas
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        ruta += caminos[gene1][gene2] 
    return ruta,

#Se minimiza con -1
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#Se define al individual como un array
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMin)
#Operaciones
toolbox = base.Toolbox()
#Generamos aleatoriamente de acuerdo al tamaño del indice
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)
# Generacion del individuo y poblacion
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#Evaluamos la función
toolbox.register("evaluate", evalPAV)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    #Definición de la semilla de generador de numero aleatorios
    random.seed(64)
    #Población inicial
    pop = toolbox.population(n=200)
    #El mejor individuo
    hof = tools.HallOfFame(1)
    #Estadísticas básicas
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True)
    return pop, stats, hof

if __name__ == "__main__":
    pop, log, hof = main()
    print("Distancia mínima: ")
    print(hof[0].fitness.values)
    print("La mejor ruta:")
    print(hof)

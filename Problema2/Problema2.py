# -*- coding: utf-8 -*-
"""
Created on Sat Dic  12 10:45:15 2020

@author: Ayax
"""

import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# Maximizar=1 o minimizar=-1
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Tipo individuo
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)
# operaciones
toolbox = base.Toolbox()

# funcion que se llena el individuo
# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)

# generacion del individuo y poblacion
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 25)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# funcion objetivo
def evalOneMax(individual):
    decimal = int("".join(map(str, individual)),2)
    x = decimal
    return ((x*x*x)+(x*x)+x),

# operaciones
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=2)

def main():
    random.seed(64)
    # genera la poblacion
    pop = toolbox.population(n=100)
    # el mejor individuo (min-max)
    hof = tools.HallOfFame(1)
    # estadisticas basicas
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=False)
    
    return pop, log, hof

if __name__ == "__main__":
    
    pop, log, hof = main()
    print(log)
    print(hof)
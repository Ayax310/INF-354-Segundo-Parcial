# -*- coding: utf-8 -*-
"""
Created on Sat Dic  12 10:45:15 2020

@author: Ayax
"""

import random

modelEnd = [6,18,1,6,20,22,28,15,5,19] 
largeIndividual = 10 

num = 5 #Cantidad de individuos
generation = 300 #Generaciones
pressure = 3 #individual>2
mutation_chance = 0.2

def individual(min, max):
    return[random.randint(min, max) for i in range(largeIndividual)]

def newPopulation():
    return [individual(0,50) for i in range(num)]

# Funcion la que se debe cambiar en funcion a f(x)
def functionType(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelEnd[i]:
            fitness += 1
    return fitness

def selection_and_reproduction(population):
    evaluating = [ (functionType(i), i) for i in population]
    print("eval",evaluating)
    evaluating = [i[1] for i in sorted(evaluating)]
    print("eval",evaluating)
    population = evaluating
    selected = evaluating[(len(evaluating)-pressure):]
    for i in range(len(population)-pressure):
        pointChange = random.randint(1,largeIndividual-1)
        father = random.sample(selected, 2)
        population[i][:pointChange] = father[0][:pointChange]
        population[i][pointChange:] = father[1][pointChange:]
    return population

def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: 
            pointChange = random.randint(1,largeIndividual-1) 
            new_val = random.randint(0,9) 
            while new_val == population[i][pointChange]:
                new_val = random.randint(0,9)
            population[i][pointChange] = new_val
    return population

def funciony(data):
    copy = []
    for elem in data:
        newdata = []
        for x in elem:
            y = (x*x*x)+(x*x)+x
            newdata.append(y)
        copy.append(newdata)
    return copy

# Principal
modelEnd.sort()
modelEnd.reverse()
print('Inicial: ', modelEnd)
print('Generaciones', generation)
population = newPopulation()
# Ordenamos descendentemente los elementos
for p in population:
    p.sort()
    p.reverse()
print("\nInicio de la población:\n%s"%(population))
population = selection_and_reproduction(population)
print("\nCruce:\n%s"%(population))
y = funciony(population)
print("\nFuncion y:\n%s" % (y))
population = mutation(population)
print("\nMutación:\n%s"%(population))

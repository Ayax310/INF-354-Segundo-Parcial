# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:51:57 2020

@author: Ayax
"""

import copy
import pandas as pd

rutas = pd.read_csv("Ejercicio1.csv",sep=',',header=None).values

matriz = rutas
print(matriz)
data = [1, 2, 3, 4]

n = len(data)
all_sets = []
g = {}
p = []

def main():
    for x in range(1, n):
        g[x + 1, ()] = matriz[x][0]

    get_minimum(1, (2,3,4))
    minimadis = get_minimum(1, (2,3,4))
    print('\n\nRuta óptima: { 1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('}')
    print('Distancia mínima')
    print(minimadis)
    return


def get_minimum(k, a):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matriz[k-1][j-1] + result)
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
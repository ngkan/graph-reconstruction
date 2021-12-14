from definitions import edges_equal
from oracles import DistanceOracle
from reconstructors import NaiveReconstructor, SimpleReconstructor
import benchmarks
from benchmarks import bench_regular_graphs
from simulate import simulate
from generators import bounded_generator, regular_generator, bounded_generator2

import networkx as nx
import matplotlib.pyplot as plt
import math
import warnings

data_path = 'data/'
regular_path = 'data/regular.txt'
bounded_path = 'data/bounded.txt'

if __name__ == "__main__":
    ds = [5, 10, 20, 50]
    ns = [100, 200, 300, 400, 500]

    # with open(regular_path, 'a') as file:
    #     for n in ns:
    #         for d in ds:
    #             print(f"Simulating n={n} d={d}.")
    #             s = int(math.log2(n)**2)
    #             print("run with", n, d, s, n*d//2)
    #             res = simulate(d, n, s, regular_generator)

    #             res = str(res)
    #             file.write(f'{d}-regular graph, {n} vertices \n')
    #             file.write(res)
    #             file.write("\n")

    # with open(bounded_path, 'a') as file:
    #     for n in ns:
    #         for d in ds:
    #             print(f"Simulating n={n} d={d}.")
    #             res = simulate(d, n, int(n**(2/3)), bounded_generator)
    #             res = str(res)
    #             file.write(f'{d}-regular graph, {n} vertices \n')
    #             file.write(res)
    #             file.write("\n")

    # with open(bounded_path, 'a') as file:
    #     for n in ns:
    #         for d in ds:
    #             print(f"Simulating n={n} d={d}.")
    #             res = simulate(d, n, int(n**(2/3)), bounded_generator2)
    #             res = str(res)
    #             file.write(f'{d}-regular graph, {n} vertices \n')
    #             file.write(res)
    #             file.write("\n")

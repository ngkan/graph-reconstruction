from definitions import edges_equal
from oracles import DistanceOracle
from reconstructors import NaiveReconstructor, SimpleReconstructor

import networkx as nx
import matplotlib.pyplot as plt

import math
import warnings


def hist_sample():
    Deltas = [5, 10, 20]
    nVs = [100, 150, 200, 250, 300]

    results = {d: {nV: [] for nV in nVs} for d in Deltas}

    nruns = 1000
    for d in Deltas:
        print(f"-- Delta = {d}")

        for nV in nVs:
            print(f"---- Number of vertices = {nV}")

            s = int(math.log2(nV))**2

            for _ in range(nruns):
                G = nx.random_regular_graph(d, nV)
                if not nx.is_connected(G):
                    print("asd")
                    continue

                oracle = DistanceOracle(G)
                reconstructor = SimpleReconstructor(s, oracle)

                count, res = reconstructor.reconstruct()

                if not edges_equal(res, G.edges):
                    warnings.warn('WRONG ANSWER!!!')

                results[d][nV].append(count)

            plt.hist(results[d][nV])
            plt.plot()
            plt.show()

        print(results[d])


def bench_regular_graphs():
    print("Benchmarking on regular graphs.")

    Deltas = [5, 10, 20]
    nVs = range(100, 1000 + 1, 50)

    results = {d: {nV: [] for nV in nVs} for d in Deltas}

    for d in Deltas:
        print(f"-- Delta = {d}")

        for nV in nVs:
            print(f"---- Number of vertices = {nV}")

            s = int(math.log2(nV))**2

            for _ in range(5):
                G = nx.random_regular_graph(d, nV)
                if not nx.is_connected(G):
                    print("asd")
                    continue

                oracle = DistanceOracle(G)
                reconstructor = SimpleReconstructor(s, oracle)

                count, res = reconstructor.reconstruct()

                if not edges_equal(res, G.edges):
                    warnings.warn('WRONG ANSWER!!!')

                results[d][nV].append(count // s)

        print(results[d])

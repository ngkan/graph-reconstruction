from definitions import edges_equal
from oracles import DistanceOracle
from reconstructors import NaiveReconstructor, SimpleReconstructor

import networkx as nx
import matplotlib.pyplot as plt

import math
import random
import warnings


def random_bounded_graph(d, n):
    """ Generate d-bounded-degree graph with n vertices by randomly removing 
    edges from a regular graph.

    pseudo:
        1) generate a regular graph
        2) choose a number k random uniformly
        3) remove k random edges uniformly
        4) repeat 1) 2) 3) until the result graph is connected

    Note: We work with n divided by 10 mostly 
    """

    while True:
        G = nx.random_regular_graph(d, n)
        k = random.uniform(0, d*n)

        toberemoved_edges = random.sample(G.edges, k)
        G.remove_edges_from(toberemoved_edges)

        if nx.is_connected(G):
            break

    return G

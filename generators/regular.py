from .base import *


def regular_generator(d, n):
    g = nx.random_regular_graph(d, n)
    while not nx.is_connected(g):
        g = nx.random_regular_graph(d, n)
    return g

from .base import *

import random


# complete binary tree ~ n sqrt(n)

def bounded_generator(d, n):
    """ Generate d-bounded-degree graph with n vertices by randomly removing 
    edges from a regular graph.

    pseudo:
        1) generate a regular graph
        2) choose a number k in [0, nd/2] random uniformly
        3) remove k random edges uniformly
        4) repeat 1) 2) 3) until the result graph is connected

    Note: We work with n divided by 10 mostly 
    """

    while True:
        G = nx.random_regular_graph(d, n)
        k = random.randint(0, d*n//2)

        toberemoved_edges = random.sample(G.edges, k)
        G.remove_edges_from(toberemoved_edges)

        if nx.is_connected(G):
            break

    return G


def bounded_generator2(d, n):
    """ Generate d-bounded-degree graph with n vertices by randomly removing 
    edges from a regular graph.

    pseudo:
        1) generate a regular graph
        2) choose a number k in [0, 2n] random uniformly
        3) remove k random edges uniformly
        4) repeat 1) 2) 3) until the result graph is connected

    Note: We work with n divided by 10 mostly 
    """

    while True:
        G = nx.random_regular_graph(d, n)
        k = random.randint(0, 2*n)

        toberemoved_edges = random.sample(G.edges, k)
        G.remove_edges_from(toberemoved_edges)

        if nx.is_connected(G):
            break

    return G

# class BoundedDegreeGenerator1(Generator):
#     """ Build a random spanning tree, then randomly choose edges """

#     def __init__(self, nvertices, delta):
#         super().__init__(nvertices)
#         self.delta = delta

#     def generate(self) -> Graph:
#         """ Will not work when delta < 2 """
#         nV = self.nV
#         nE = nV * 3  # number of edges
#         edges = []

#         taken = set()
#         counts = {u: self.delta for u in range(nV)}

#         # build a spanning tree first
#         for u in range(1, nV):
#             p = -1
#             while p not in counts:
#                 p = random.choice(0, u)

#             counts[p] -= 1
#             counts[u] -= 1

#             nE -= 1
#             edges.append((p, u))
#             taken.add((p, u))

#             if counts[p] == 0:
#                 counts.pop(p)

#         # randomly add edges

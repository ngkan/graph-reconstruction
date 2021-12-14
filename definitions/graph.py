import networkx as nx

import warnings
import json

Edges = list[int, int]


def edges_equal(lista: Edges, listb: Edges):
    """ Comparing two lists of edges (without duplications) """
    seta = set()
    for (x, y) in lista:
        if x > y:
            x, y = y, x

        seta.add((x, y))

    setb = set()
    for (x, y) in listb:
        if x > y:
            x, y = y, x

        setb.add((x, y))

    return (seta == setb)


class Graph(nx.Graph):
    """
    Python representation of graphs (connected, undirected, unweighted) based on
    networkx package.

    From networkx's description of nx.Graph:
        Graphs hold undirected edges. 
        Self loops are allowed but multiple (parallel) edges are not.

    Here we define:
        Vertices to be integers indexed consecutively from 0.
        Edges to be a list of pairs of integers without duplications and self-loops.
    """

    def __init__(self, nV: int, edges: Edges, name: str = None):
        super().__init__(name=name)

        # Using written methods to initialize graph
        self.add_nodes_from(range(nV))
        self.add_edges_from(edges)

        # Warning if constraints are not followed
        if self.number_of_nodes() != nV:
            warnings.warn('Warning: {self.name}\'s edges contain nodes that are out-of-range.')
        if not nx.is_connected(self):
            warnings.warn('Warning: {self.name} is not connencted.')
        if self.number_of_selfloops() > 0:
            warnings.warn('Warning: {self.name} has self-loops.')


# class Graph:
#     """
#     Python representation of graphs (connected, undirected, unweighted) .
#     Vertices are integers indexed consecutively from 0.
#     Edges are a list of pairs of integers without duplications and self-loops.
#     """

#     def __init__(self, nvertices, edges, name=None):
#         self.name = name if name is not None else "Graph"
#         self.nV = nvertices
#         self.nE = len(edges)
#         self.edges = edges
#         self.adj = [[] for _ in range(nvertices)]   # adjacency lists

#         self.edges_verifying()

#         for (u, v) in edges:
#             self.adj[u].append(v)
#             self.adj[v].append(u)

#         if not self.is_connected():
#             warnings.warn('Warning: {self.name} is not connected')

#     def edges_verifying(self):
#         """ Vertices are valid, no edges duplications, no self-loop """
#         count = dict()

#         for (u, v) in self.edges:
#             if u > v:
#                 u, v = v, u

#             if u == v:
#                 warnings.warn('Warning: {self.name} has a self-loop: ({u}, {v}).')
#             if (not (0 <= u < self.nv)) or (not (0 <= u < self.nV)):
#                 warnings.warn('Warning: {self.name} has an invalid edge: ({u}, {v}).')

#             if (u, v) not in count:
#                 count[(u, v)] = 1
#             elif count[(u, v)] == 1:
#                 warnings.warn('Warning: {self.name} has a duplicated edge: ({u}, {v}).')
#                 count[(u, v)] = 2

#     def is_connected(self):
#         """ DFS """
#         visited = [False] * self.nV
#         visited[0] = 1
#         stack = [0]

#         while stack:
#             u = stack.pop()
#             for v in self.adj[u]:
#                 if not visited[v]:
#                     visited[v] = True
#                     stack.append(v)

#         return not (False in visited)

#     def write(self, folder_path='tests'):
#         data = {
#             'name': self.name,
#             'nvertices': self.nV,
#             'nedges': self.nE,
#             'edges': self.edges
#         }

#         with open(f'{folder_path}/{self.name}.json', 'w') as f:
#             json.dump(data, f)


# def graph_from_file(path):
#     with open(path, 'r') as f:
#         data = json.loads(f.read())

#     return Graph(data['nvertices'], data['edges'], data['name'])

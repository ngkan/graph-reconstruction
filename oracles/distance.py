from .base import *


class DistanceOracle(Oracle):
    def __init__(self, graph):
        super().__init__(graph)
        self.dist = dict(nx.all_pairs_shortest_path_length(self.graph))

    def query(self, a, b):
        self.query_count += 1
        return self.dist[a][b]

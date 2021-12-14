from oracles.base import Oracle
from definitions import Edges, Graph
from oracles import Oracle, DistanceOracle


class BaseReconstructor:
    def __init__(self, oracle: Oracle):
        self.nV = oracle.graph.number_of_nodes()
        self.oracle = oracle

    def reconstruct(self) -> Edges:
        raise NotImplementedError

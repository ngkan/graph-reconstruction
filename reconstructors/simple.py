from .base import BaseReconstructor

from definitions import Edges, Graph
from oracles import Oracle

import random
import warnings
warnings.simplefilter('always', UserWarning)


class SimpleReconstructor(BaseReconstructor):
    def __init__(self, s: int, oracle: Oracle):
        super().__init__(oracle)
        self.s = s

        if s > oracle.graph.number_of_nodes():
            warnings.warn('Warning: SimpleReconstructor is invalid: s ({self.s}) is greater than the number of nodes ({self.nV}).')

    def reconstruct(self) -> tuple[int, Edges]:
        self.oracle.reset_query_count()
        result = []

        S = random.sample(range(self.nV), k=self.s)
        V = range(self.nV)

        d = [[None for _ in range(self.nV)] for _ in range(self.nV)]

        for u in S:
            for v in V:
                d[u][v] = self.oracle.query(u, v)

        E_hat = []
        for a in V:
            for b in range(a+1, self.nV):
                interesting = True

                for u in S:
                    if abs(d[u][a] - d[u][b]) > 1:
                        interesting = False

                if interesting:
                    E_hat.append((a, b))

        for (a, b) in E_hat:
            if self.oracle.query(a, b) == 1:
                result.append((a, b))

        return (self.oracle.query_count, result)

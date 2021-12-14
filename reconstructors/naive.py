from definitions import Edges, Graph
from .base import BaseReconstructor


class NaiveReconstructor(BaseReconstructor):
    def __init__(self, oracle):
        super().__init__(oracle)

    def reconstruct(self) -> tuple[int, Edges]:
        self.oracle.reset_query_count()
        result = []

        for a in range(0, self.nV):
            for b in range(a + 1, self.nV):
                if self.oracle.query(a, b) == 1:
                    result.append((a, b))

        return (self.oracle.query_count, result)

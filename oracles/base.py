from definitions import *

from math import inf as INF
from collections import deque


class Oracle:
    def __init__(self, graph):
        self.graph = graph
        self.query_count = 0

    def query(self, a, b):
        raise NotImplementedError

    def reset_query_count(self):
        self.query_count = 0

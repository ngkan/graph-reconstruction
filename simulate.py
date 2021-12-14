from definitions import edges_equal
from oracles import DistanceOracle
from reconstructors import SimpleReconstructor

import warnings
warnings.simplefilter('always', UserWarning)


def run(s, G):
    oracle = DistanceOracle(G)
    reconstructor = SimpleReconstructor(s, oracle)
    count, res = reconstructor.reconstruct()

    if not edges_equal(res, G.edges):
        warnings.warn('WRONG ANSWER!!!')

    return count


def simulate(d, n, s, generator, ndatapoints=200):
    results = []

    while ndatapoints > 0:
        ndatapoints -= 1

        G = generator(d, n)
        results.append(run(s, G))

    return results

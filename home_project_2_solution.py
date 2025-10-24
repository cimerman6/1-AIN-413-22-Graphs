#skusime klasicky algoritmus kde jednoducho len prehladame vsetky moznosti a hladame najvacsi ciastocny automorfizmus
#dufam ze sme mohli pouzit itertools co nam velmi ulahcilo generovanie kombinacii

import itertools
import networkx as nx
# you are allowed to use any function in networkx library including nx.is_isomorphic, nx.vf2pp_all_isomorphisms, etc.

def asymmetric_depth(Graph) -> int:
    n = len(Graph.nodes)
    vrcholy = list(Graph.nodes)
    maximum = 0

    for k in range(n, 0, -1):
        for subset1 in itertools.combinations(vrcholy, k): #vsetky kombinacie s k prvkami
            G1 = Graph.subgraph(subset1)
            zostavajuce = list(set(vrcholy) - set(subset1))

            for subset2 in itertools.combinations(zostavajuce, k):
                G2 = Graph.subgraph(subset2)

                if nx.is_isomorphic(G1, G2):
                    if k > maximum:
                        maximum = k

    return n - maximum

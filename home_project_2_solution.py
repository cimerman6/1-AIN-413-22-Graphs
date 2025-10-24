#skusime klasicky algoritmus kde jednoducho len prehladame vsetky moznosti a hladame najvacsi ciastocny automorfizmus
#dufam ze sme mohli pouzit itertools co nam velmi ulahcilo generovanie kombinacii

import itertools
import networkx as nx

def asymmetric_depth(Graph) -> int:
    n = len(Graph.nodes)
    vrcholy = list(Graph.nodes)
    maximum = 0

    for k in range(n, 0, -1):
        for subset1 in itertools.combinations(vrcholy, k):
            G1 = Graph.subgraph(subset1)

            for subset2 in itertools.combinations(vrcholy, k):
                G2 = Graph.subgraph(subset2)
                rovnake = set(subset1) == set(subset2)

                for x in nx.vf2pp_all_isomorphisms(G1, G2):
                    if rovnake:
                        identita = True
                        for v in x:
                            if x[v] != v:
                                identita = False
                                break
                        if not identita:
                            maximum = max(maximum, k)
                            break

                    else:
                        maximum = max(maximum, k)
                        break

    return n - maximum


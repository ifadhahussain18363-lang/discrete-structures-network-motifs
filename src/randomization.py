
import random
from collections import Counter


def get_degrees(edges):
    """Calculate in-degree and out-degree for every node."""
    in_degree = Counter()
    out_degree = Counter()

    for source, target in edges:
        out_degree[source] += 1
        in_degree[target] += 1

    return in_degree, out_degree


def randomize(edges, attempts, seed):
    """
    Randomize a directed graph using double-edge swaps.

    Preserves every node's in-degree and out-degree.
    Rejected swaps still count as attempts.
    """
    randomized_edges = set(edges)

    original_in, original_out = get_degrees(randomized_edges)

    rng = random.Random(seed)

    for _ in range(attempts):
        if len(randomized_edges) < 2:
            break

        edge1, edge2 = rng.sample(list(randomized_edges), 2)

        a, b = edge1
        c, d = edge2

        # Proposed replacement edges
        new_edge1 = (a, d)
        new_edge2 = (c, b)

        # Reject self-loops
        if a == d or c == b:
            continue

        # Reject duplicate edges
        remaining_edges = randomized_edges - {edge1, edge2}

        if new_edge1 in remaining_edges:
            continue

        if new_edge2 in remaining_edges:
            continue

        if new_edge1 == new_edge2:
            continue

        # Perform the double-edge swap
        randomized_edges.remove(edge1)
        randomized_edges.remove(edge2)

        randomized_edges.add(new_edge1)
        randomized_edges.add(new_edge2)

    # Verify degree preservation
    final_in, final_out = get_degrees(randomized_edges)

    assert original_in == final_in
    assert original_out == final_out

    return randomized_edges

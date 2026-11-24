
from itertools import permutations

# Each bit represents a possible directed edge.
BIT_EDGES = [
    (0, 1),  # Bit 0: 0 -> 1
    (0, 2),  # Bit 1: 0 -> 2
    (1, 0),  # Bit 2: 1 -> 0
    (1, 2),  # Bit 3: 1 -> 2
    (2, 0),  # Bit 4: 2 -> 0
    (2, 1)   # Bit 5: 2 -> 1
]

# Canonical code to triad class mapping.
CLASS_BY_CODE = {
    3: 1,
    6: 2,
    7: 3,
    10: 4,
    11: 5,
    15: 6,
    21: 7,
    23: 8,
    25: 9,
    27: 10,
    30: 11,
    31: 12,
    63: 13
}


def canonical_code(a, b, c, edges):
    nodes = (a, b, c)

    if len(set(nodes)) != 3:
        raise ValueError("A triad must contain three different nodes.")

    minimum_code = 64

    for ordering in permutations(nodes):
        code = 0

        for bit, (src, dst) in enumerate(BIT_EDGES):
            source_node = ordering[src]
            destination_node = ordering[dst]

            if (source_node, destination_node) in edges:
                code |= (1 << bit)

        minimum_code = min(minimum_code, code)

    return minimum_code


def triad_class(a, b, c, edges):
    code = canonical_code(a, b, c, edges)

    if code not in CLASS_BY_CODE:
        raise ValueError(f"Disconnected triad or invalid code: {code}")

    return CLASS_BY_CODE[code]

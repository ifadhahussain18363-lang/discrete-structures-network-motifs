
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from triad_classification import (
    triad_class,
    canonical_code,
    CLASS_BY_CODE,
    BIT_EDGES
)

# Test 1: Simple Class 1 example
edges = {
    ("A", "B"),
    ("A", "C")
}

result = triad_class("A", "B", "C", edges)
assert result == 1

# Test 2: Verify all 13 canonical codes
nodes = (0, 1, 2)

for code, expected_class in CLASS_BY_CODE.items():
    edges = set()

    for bit, (src, dst) in enumerate(BIT_EDGES):
        if code & (1 << bit):
            edges.add((nodes[src], nodes[dst]))

    actual_class = triad_class(
        nodes[0], nodes[1], nodes[2], edges
    )

    assert actual_class == expected_class

# Test 3: All six permutations must give the same class
from itertools import permutations

edges = {("A", "B"), ("A", "C")}

for ordering in permutations(("A", "B", "C")):
    assert triad_class(*ordering, edges) == 1

# Test 4: Disconnected triad must be rejected
try:
    triad_class("A", "B", "C", {("A", "B")})
    raise AssertionError("Expected ValueError")
except ValueError:
    pass

print("Test 1 passed: Class 1")
print("Test 2 passed: All 13 classes")
print("Test 3 passed: All six permutations")
print("Test 4 passed: Disconnected triad rejected")
print("\nAll classification tests passed!")

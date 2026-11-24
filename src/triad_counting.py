
from itertools import combinations
from pathlib import Path

from triad_classification import triad_class


def read_nodes(filename):
    """Read node IDs from a text file."""
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file if line.strip()]


def read_edges(filename):
    """Read directed edges from a text file."""
    edges = set()

    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                source, destination = map(int, line.split())
                edges.add((source, destination))

    return edges


def count_triads(nodes, edges):
    """Count all 13 connected triad classes in a directed network."""

    nodes = list(nodes)
    edge_set = set(edges)

    adjacency = {node: set() for node in nodes}

    for source, destination in edge_set:
        if source not in adjacency or destination not in adjacency:
            raise ValueError(
                "An edge contains a node missing from the node list."
            )

        if source == destination:
            raise ValueError(
                "Self-loops must be removed before counting."
            )

        adjacency[source].add(destination)
        adjacency[destination].add(source)

    counts = {class_number: 0 for class_number in range(1, 14)}
    seen_triads = set()

    for center in nodes:
        neighbors = adjacency[center]

        for node_a, node_b in combinations(neighbors, 2):
            triad = tuple(sorted((center, node_a, node_b)))

            if triad in seen_triads:
                continue

            seen_triads.add(triad)

            class_number = triad_class(
                triad[0],
                triad[1],
                triad[2],
                edge_set
            )

            counts[class_number] += 1

    return counts


def main():
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "output"

    departments = {
        "Department A": (
            "department_A_nodes.txt",
            "department_A_edges.txt"
        ),
        "Department B": (
            "department_B_nodes.txt",
            "department_B_edges.txt"
        )
    }

    for department, filenames in departments.items():

        nodes_file = data_dir / filenames[0]
        edges_file = data_dir / filenames[1]

        nodes = read_nodes(nodes_file)
        edges = read_edges(edges_file)

        counts = count_triads(nodes, edges)

        print("\n" + department)
        print("-------------------------")
        print("Triad Class | Count")

        for class_number, count in counts.items():
            print(f"{class_number:11} | {count}")

        print("Total connected triads:", sum(counts.values()))


if __name__ == "__main__":
    main()

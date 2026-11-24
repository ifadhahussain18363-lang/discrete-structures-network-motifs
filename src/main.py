
from pathlib import Path
from data import load_and_clean_data, count_internal_edges, get_top20


# GROUP PROJECT PARAMETERS
R = 9685

NUMBER_OF_RANDOM_NETWORKS = 20 + (R % 31)
SWAP_MULTIPLIER = 5 + (R % 6)
RANDOM_SEED = R


def select_departments(top20, R):

    pairs = []

    # Generate all 190 pairs in lexicographic order
    for i in range(20):
        for j in range(i + 1, 20):
            pairs.append((i, j))

    pair_index = R % 190

    i, j = pairs[pair_index]

    department_A = top20[i][0]
    department_B = top20[j][0]

    return pair_index, department_A, department_B


def create_subgraph(edges, departments, department_id):

    # Find all people belonging to this department
    nodes = {
        node
        for node, dept in departments.items()
        if dept == department_id
    }

    # Keep only edges where both people belong to this department
    subgraph_edges = {
        (u, v)
        for u, v in edges
        if u in nodes and v in nodes
    }

    return nodes, subgraph_edges


def save_subgraph(nodes, edges, department_id, label):

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    # Save nodes
    with open(
        output_folder / f"department_{label}_nodes.txt", "w"
    ) as file:

        for node in sorted(nodes):
            file.write(f"{node}\n")

    # Save edges
    with open(
        output_folder / f"department_{label}_edges.txt", "w"
    ) as file:

        for u, v in sorted(edges):
            file.write(f"{u} {v}\n")

    print(f"\nDepartment {label} (ID {department_id})")
    print("Number of people:", len(nodes))
    print("Number of internal edges:", len(edges))


def main():

    # Load cleaned network
    edges, departments = load_and_clean_data()

    # Find top 20 departments
    internal_counts = count_internal_edges(edges, departments)
    top20 = get_top20(internal_counts)

    # Select departments
    pair_index, department_A, department_B = select_departments(
        top20, R
    )

    print("\nPROJECT PARAMETERS")
    print("R:", R)
    print("Pair index:", pair_index)
    print("Department A:", department_A)
    print("Department B:", department_B)
    print("Number of random networks:", NUMBER_OF_RANDOM_NETWORKS)
    print("Swap multiplier:", SWAP_MULTIPLIER)
    print("Random seed:", RANDOM_SEED)

    # Create both department subgraphs
    nodes_A, edges_A = create_subgraph(
        edges, departments, department_A
    )

    nodes_B, edges_B = create_subgraph(
        edges, departments, department_B
    )

    # Save both subgraphs
    save_subgraph(nodes_A, edges_A, department_A, "A")
    save_subgraph(nodes_B, edges_B, department_B, "B")

    # Save project parameters
    with open("output/project_parameters.txt", "w") as file:

        file.write(f"R = {R}\n")
        file.write(f"Pair index = {pair_index}\n")
        file.write(f"Department A = {department_A}\n")
        file.write(f"Department B = {department_B}\n")
        file.write(
            f"Number of random networks = "
            f"{NUMBER_OF_RANDOM_NETWORKS}\n"
        )
        file.write(f"Swap multiplier = {SWAP_MULTIPLIER}\n")
        file.write(f"Random seed = {RANDOM_SEED}\n")

    print("\nAll subgraph files saved successfully!")


if __name__ == "__main__":
    main()

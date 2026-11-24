
import csv
from pathlib import Path


def load_and_clean_data():

    dataset_folder = Path("dataset")

    email_file = dataset_folder / "email-Eu-core.txt"
    department_file = dataset_folder / "email-Eu-core-department-labels.txt"

    # Read and clean email connections
    edges = set()

    raw_rows = 0
    self_loops = 0
    duplicate_rows = 0

    with open(email_file, "r") as file:
        for line in file:
            raw_rows += 1

            u, v = map(int, line.split())

            if u == v:
                self_loops += 1

            elif (u, v) in edges:
                duplicate_rows += 1

            else:
                edges.add((u, v))

    # Read department labels
    departments = {}

    with open(department_file, "r") as file:
        for line in file:
            node, department = map(int, line.split())
            departments[node] = department

    # Check for missing department labels
    missing = set()

    for u, v in edges:
        if u not in departments:
            missing.add(u)

        if v not in departments:
            missing.add(v)

    if missing:
        raise ValueError(
            f"Nodes missing department labels: {len(missing)}"
        )

    print("\nDATA CLEANING RESULTS")
    print("Original rows:", raw_rows)
    print("Self-loops removed:", self_loops)
    print("Duplicate edges removed:", duplicate_rows)

    print("\nDATA LOADED SUCCESSFULLY")
    print("People:", len(departments))
    print("Clean email connections:", len(edges))
    print("Departments:", len(set(departments.values())))

    return edges, departments


def count_internal_edges(edges, departments):

    counts = {}

    for department in set(departments.values()):
        counts[department] = 0

    for u, v in edges:

        if departments[u] == departments[v]:
            counts[departments[u]] += 1

    return counts


def get_top20(internal_counts):

    ranked = sorted(
        internal_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return ranked[:20]


def save_results(edges, internal_counts, top20):

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    # Save cleaned edges
    with open(output_folder / "cleaned_edges.txt", "w") as file:

        for u, v in sorted(edges):
            file.write(f"{u} {v}\n")

    # Save department counts
    with open(
        output_folder / "department_counts.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)
        writer.writerow(["Department", "Internal_Edges"])

        for department, count in sorted(internal_counts.items()):
            writer.writerow([department, count])

    # Save top 20 departments
    with open(output_folder / "top20_departments.txt", "w") as file:

        for rank, (department, count) in enumerate(top20, start=1):
            file.write(
                f"{rank}. Department {department}: {count} edges\n"
            )


if __name__ == "__main__":

    edges, departments = load_and_clean_data()

    internal_counts = count_internal_edges(edges, departments)

    top20 = get_top20(internal_counts)

    save_results(edges, internal_counts, top20)

    print("\nTOP 20 DEPARTMENTS")

    for rank, (department, count) in enumerate(top20, start=1):

        print(
            f"{rank}. Department {department}: "
            f"{count} internal edges"
        )

    print("\nResults saved in the output folder.")

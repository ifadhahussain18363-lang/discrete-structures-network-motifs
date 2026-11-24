
import csv
import statistics
from pathlib import Path

from randomization import randomize
from triad_counting import read_nodes, read_edges, count_triads


R = 9685
NUMBER_OF_RANDOM_NETWORKS = 33
SWAP_MULTIPLIER = 6
RANDOM_SEED = R


def analyze_department(label):
    output_dir = Path("output")

    nodes = read_nodes(output_dir / f"department_{label}_nodes.txt")
    original_edges = read_edges(
        output_dir / f"department_{label}_edges.txt"
    )

    # Count triads in the original network
    observed = count_triads(nodes, original_edges)

    # Generate 33 randomized networks
    random_counts = {i: [] for i in range(1, 14)}
    attempts = SWAP_MULTIPLIER * len(original_edges)

    for network_number in range(NUMBER_OF_RANDOM_NETWORKS):
        # Every network starts from the original edge set
        randomized_edges = randomize(
            original_edges,
            attempts,
            RANDOM_SEED + network_number
        )

        counts = count_triads(nodes, randomized_edges)

        for triad_class in range(1, 14):
            random_counts[triad_class].append(
                counts[triad_class]
            )

    # Calculate mean, population SD and Z-score
    results = []

    for triad_class in range(1, 14):
        values = random_counts[triad_class]

        mean = statistics.mean(values)
        population_sd = statistics.pstdev(values)

        if population_sd == 0:
            z_score = 0
        else:
            z_score = (
                observed[triad_class] - mean
            ) / population_sd

        if z_score > 2:
            classification = "Motif"
        elif z_score < -2:
            classification = "Anti-motif"
        else:
            classification = "Neither"

        results.append([
            triad_class,
            observed[triad_class],
            round(mean, 4),
            round(population_sd, 4),
            round(z_score, 4),
            classification
        ])

    # Save the department's Z-score table
    filename = output_dir / f"department_{label}_z_scores.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Triad Class",
            "Observed Count",
            "Random Mean",
            "Population SD",
            "Z-score",
            "Result"
        ])
        writer.writerows(results)

    print(f"\nDepartment {label}")
    print("Edges:", len(original_edges))
    print("Swap attempts per network:", attempts)
    print("Random networks:", NUMBER_OF_RANDOM_NETWORKS)
    print("Saved:", filename)

    for row in results:
        print(row)


def main():
    analyze_department("A")
    analyze_department("B")


if __name__ == "__main__":
    main()

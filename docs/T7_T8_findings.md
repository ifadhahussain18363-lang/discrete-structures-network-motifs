# Person 4 — T7 and T8: Chart and Interpretation

## T7: Z-score comparison chart

The grouped bar chart compares the Z-scores of all 13 connected triad classes in Department A (department ID 8) and Department B (department ID 37).

- The horizontal dashed line at +2 is the motif threshold.
- The horizontal dashed line at -2 is the anti-motif threshold.
- A bar above +2 indicates a motif: that triad appears significantly more often than in the randomized networks.
- A bar below -2 indicates an anti-motif: that triad appears significantly less often than in the randomized networks.
- Values between -2 and +2 are classified as neither.

The chart is saved as `output/department_triad_motif_z_scores.png`.

## T8: Findings and interpretation

Both departments have the same two motif classes: **Class 8** and **Class 13**. This means these two three-person communication structures occur more often than expected under the degree-preserving randomized-network comparison in both departments.

Both departments also share three anti-motif classes: **Classes 1, 2, and 10**. These structures occur less often than expected in both departments.

Department A (ID 8) has additional anti-motifs in **Classes 6, 7, and 12**. Department B (ID 37) has additional anti-motifs in **Classes 4 and 5**. The remaining classes are neither motifs nor anti-motifs for the relevant department.

Overall, the two departments show some similarities because they share motif classes 8 and 13 and anti-motif classes 1, 2, and 10. However, their additional anti-motif classes differ, suggesting that some smaller-group email communication patterns are not equally common in the two departments. These results describe patterns in the observed email network; they do not by themselves explain why employees communicate this way.

## Classification details from the supplied result files

| Triad class | Department A (ID 8) | Department B (ID 37) |
|---|---:|---:|
| 1 | -2.8081 (Anti-motif) | -2.0198 (Anti-motif) |
| 2 | -2.2217 (Anti-motif) | -3.8861 (Anti-motif) |
| 3 | -0.0668 (Neither) | 0.2669 (Neither) |
| 4 | -1.4769 (Neither) | -2.7190 (Anti-motif) |
| 5 | 0.0000 (Neither) | -2.4817 (Anti-motif) |
| 6 | -2.3436 (Anti-motif) | -1.1418 (Neither) |
| 7 | -3.5411 (Anti-motif) | -0.2349 (Neither) |
| 8 | 3.8340 (Motif) | 4.6454 (Motif) |
| 9 | -1.2232 (Neither) | -1.6723 (Neither) |
| 10 | -3.2002 (Anti-motif) | -3.6600 (Anti-motif) |
| 11 | 0.3582 (Neither) | -1.8014 (Neither) |
| 12 | -3.0636 (Anti-motif) | -1.6033 (Neither) |
| 13 | 4.4508 (Motif) | 3.2988 (Motif) |


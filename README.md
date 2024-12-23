# Max Matrix Population Path

The matrix population path problem involves finding the maximum population sum by traversing a 2D matrix, where each cell represents a city's population. Starting from any cell in the first column, you can move to a neighboring cell (above, below, or the same row) in the next column, continuing until the last column. The goal is to determine the path that yields the highest total population. This problem exhibits optimal substructure, making it solvable using dynamic programming, where the value at each cell represents the maximum population sum achievable up to that point. Once the DP table is built, the optimal path can be reconstructed by tracing the maximum values row by row.

---

## Phase 1: Raw Problem

This code solves the matrix population path problem using a **dynamic programming (DP)** approach to compute the maximum population sum and reconstruct the optimal path. It starts by transposing the input matrix (`city_t`) to simplify column-based traversal. The `dp` table stores the maximum population sum achievable at each cell starting from that position, while the `parent` table tracks the column index of the cell in the next row contributing to the optimal path.

The **base case** initializes the last row of `dp` to the corresponding values in `city_t`, as no further rows exist to contribute. The DP recurrence relation iteratively fills the table from the second-to-last row up to the first, computing each cell as the sum of its population and the maximum value from the three valid neighboring cells in the next row. The `parent` table simultaneously records which neighbor was chosen, enabling efficient path reconstruction.

After computing the DP table, the optimal path is reconstructed starting from the cell in the first row with the maximum `dp` value. The algorithm traces through the `parent` table row by row, building the optimal path efficiently. Although the commented-out greedy method is included as an alternative, it is not used in the current implementation. The result includes the maximum population sum and the optimal path, printed as space-separated indices.

- **Greedy Path Reconstruction**
The commented-out greedy method for reconstructing the path without explicitly using the `parent` table. Instead, it traces the maximum values dynamically during the traversal of the `city_t` matrix. While this approach is more memory-efficient, it relies on the correctness of the DP table's values and can miss some intermediate details about how decisions were made. By contrast, constructing the `parent` table ensures an explicit and reliable mapping of the optimal transitions, making the path reconstruction both efficient and straightforward.

## Phase 2: Recharge Stations

In the second phase of the problem, the goal remains to find the path with the maximum population sum, but with an added constraint: if a column contains at least one city marked as `X`, the path must pass through one of the cities marked as `O` in that column. Cities marked as `X` are considered impassable, while cities marked as `O` are mandatory checkpoints for paths traversing constrained columns. This introduces a layer of complexity, as valid paths must now account for both maximizing the population sum and satisfying these mandatory constraints.

`phase_2.py` addresses the added problem by using a flag, `re_freeze`, to detect when a column contains one or more `X` values. For constrained columns, cities marked as `X` are assigned a population of zero in the DP table, effectively removing them from consideration. The algorithm then ensures that only paths passing through cities marked as `O` are included in the DP computation. For unconstrained columns, the original DP logic is applied as before. The `parent` table is updated accordingly to track the optimal transitions while adhering to the constraints, allowing the reconstruction of the valid maximum path that satisfies the new rules.

## Phase 3: Lazy Turns

In the final phase of the problem, the goal is to find the maximum population path while incorporating preferences for traversal directions. Straight (vertical) movements are rewarded with an additional score of +1, while diagonal movements (both left and right) incur a penalty of -1. This phase builds on the second phase by retaining the constraints related to `X` and `O` cities while factoring in the traversal preferences to maximize the overall score.

The code addresses these traversal preferences by adjusting the DP recurrence relation. During the computation, each potential move (diagonal-left, straight, diagonal-right) is evaluated, with penalties or bonuses applied based on the movement direction. The `dp` table stores these adjusted scores, ensuring that the path calculation accounts for both population sums and traversal preferences. The `parent` table is updated to track the best moves while adhering to constraints and preferences. The reconstructed path prioritizes straight movements whenever possible while satisfying the constraints imposed by `X` and `O` cities. By integrating traversal preferences directly into the DP calculation, the algorithm efficiently solves the problem while maintaining clarity and adaptability.

---

## Complexity Analysis

This project can be broken down into several components, each with its own computational complexity. First, reading the input matrix and preprocessing it to replace `X` and `O` with their respective markers (`-1` and `-2`) has a complexity of \(O(n \times m)\), where \(n\) is the number of rows and \(m\) is the number of columns. The core DP computation involves iterating through each cell of the matrix starting from the second-to-last row, calculating the optimal path value for each cell by comparing up to three possible moves. This results in a complexity of \(O(n \times m)\) for filling the `dp` and `parent` tables. Reconstructing the path from the `parent` table requires a single traversal from the top to the bottom of the matrix, which has a complexity of \(O(n)\). The overall complexity of the project is therefore dominated by the \(O(n \times m)\) DP computation phase, making it efficient and scalable for reasonably large matrices.

---

## Conclusion

Across the three phases, the problem evolves from a straightforward optimization of population sums to incorporating progressively complex constraints and preferences. The first phase establishes the foundation by computing the maximum population path using a DP approach. The second phase introduces mandatory constraints requiring paths to pass through specific cities (`O`) when encountering restricted columns (`X`). Finally, the third phase adds directional preferences, rewarding straight movements and penalizing diagonal ones, while still respecting all prior constraints. Together, these phases demonstrate the flexibility and power of dynamic programming in solving layered optimization problems with multiple interdependent factors.

---

- **Regards**
*Erfan Rajati Haghi*
*Yasaman Ohadi*
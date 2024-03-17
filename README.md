# AI Searching Algorithms Repository

This repository contains various AI searching algorithms implemented in Python, each organized into separate folders. The focus of this repository is on providing simple and easy-to-understand implementations of different search algorithms.

## Types of Search Algorithms

### Uninformed/Blind Search
Uninformed search, also known as Blind Search, operates without any domain knowledge regarding the search space. It explores the search tree in a brute-force manner, examining each node until it reaches the goal node.

#### Types of Uninformed Search:
1. **Breadth-first search**: Explores all nodes at the current depth before moving to the next level.
2. **Uniform cost search**: Expands the node with the lowest path cost.
3. **Depth-first search**: Explores as far as possible along each branch before backtracking.
4. **Iterative deepening depth-first search**: Repeatedly applies depth-first search with increasing depth limits.
5. **Bidirectional Search**: Simultaneously explores the search space from the start and goal nodes.

### Informed Search
Informed search, also known as Heuristic search, utilizes domain knowledge to guide the search process. These algorithms make use of problem-specific information to find solutions more efficiently.

Informed search strategies can handle more complex problems compared to uninformed search strategies, as they are capable of making informed decisions rather than relying solely on blind exploration.

#### Types of Informed Search:
1. **Greedy Search**: Selects the path that appears to be the best at the current moment without considering the global view.
2. **A* Search**: Utilizes both the cost to reach the current node and an estimate of the cost to reach the goal from that node. It guarantees to find the optimal solution if certain conditions are met.

## Examples
An example of an informed search algorithm is the traveling salesman problem, where the heuristic provides an estimate of the minimum distance to cover all cities.

## Contributions
Contributions to this repository are welcome! Feel free to add implementations of additional search algorithms or improve existing ones.

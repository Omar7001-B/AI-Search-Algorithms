# Uninformed Search Algorithms 🔎

This directory contains implementations of various uninformed (blind) search algorithms. These algorithms perform systematic exploration without using any problem-specific knowledge or heuristics.

## Available Algorithms

### 1. Breadth-First Search (BFS)
- **Description**: Explores all nodes at present depth before moving to next level
- **Use Case**: Finding shortest path in unweighted graphs
- **Location**: `/BFS/`

### 2. Depth-First Search (DFS)
- **Description**: Explores as far as possible along each branch before backtracking
- **Use Case**: Maze solving, topological sorting
- **Location**: `/DFS/`

### 3. Depth-Limited Search (DLS)
- **Description**: DFS with a pre-defined depth limit
- **Use Case**: When solution depth is known
- **Location**: `/DLS/`

### 4. Iterative Deepening DFS (IDDFS)
- **Description**: Repeatedly applies DLS with increasing depth limits
- **Use Case**: Combines benefits of BFS and DFS
- **Location**: `/IDDFS/`

### 5. Uniform Cost Search (UCS)
- **Description**: Explores paths based on their cumulative cost
- **Use Case**: Finding cheapest path in weighted graphs
- **Location**: `/UCS/`

### 6. Dijkstra's Algorithm
- **Description**: Finds shortest paths between nodes in a weighted graph
- **Use Case**: Network routing, GPS navigation
- **Location**: `/Dijkstra/`

## Key Characteristics
- No problem-specific knowledge used
- Complete but potentially inefficient
- Guaranteed to find solution if one exists
- Memory usage varies by algorithm

## Common Applications
- Graph traversal
- Network routing
- Maze solving
- State space exploration 
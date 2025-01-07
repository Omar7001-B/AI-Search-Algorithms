# Breadth-First Search (BFS) Algorithm 🌳

BFS is a fundamental graph traversal algorithm that explores a graph level by level.

## How It Works
- Starts at a root node
- Explores all neighbors at current depth
- Moves to next level only after current level is complete
- Uses a queue data structure (FIFO)

## Features
- Guarantees shortest path in unweighted graphs
- Complete: Will find solution if it exists
- Optimal for unweighted graphs
- Time Complexity: O(V + E)
- Space Complexity: O(V)

## Implementation Details
- Uses Queue for frontier management
- Maintains visited set to avoid cycles
- Implements path reconstruction
- Handles both directed and undirected graphs

## Usage
Run `BFS.py` with your graph input to find shortest paths. 
# Depth-First Search (DFS) Algorithm 🌲

DFS is a graph traversal algorithm that explores as deeply as possible along each branch before backtracking.

## How It Works
- Starts at a root node
- Explores one branch completely before backtracking
- Uses stack data structure (LIFO)
- Can be implemented recursively or iteratively

## Features
- Memory efficient for deep graphs
- Not guaranteed to find shortest path
- Complete for finite graphs
- Time Complexity: O(V + E)
- Space Complexity: O(h) where h is height

## Implementation Details
- Uses Stack for frontier management
- Maintains visited set to avoid cycles
- Can be used for:
  - Topological Sorting
  - Finding connected components
  - Maze generation/solving

## Usage
Run `DFS.py` with your graph input to explore depth-first traversal. 
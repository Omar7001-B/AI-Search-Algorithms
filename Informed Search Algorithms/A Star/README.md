# A* Search Algorithm ⭐

A* (A-Star) is an informed search algorithm that combines the benefits of both Dijkstra's algorithm and Best-First Search.

## How It Works
A* uses the formula: f(n) = g(n) + h(n)
- g(n): Actual cost from start node to current node
- h(n): Estimated cost from current node to goal (heuristic)
- f(n): Total estimated cost of path through node n

## Features
- Guarantees shortest path when using admissible heuristics
- Optimal performance among algorithms with same heuristic
- Explores the most promising paths first

## Implementation Details
- Uses priority queue for efficient node selection
- Implements path reconstruction
- Includes Manhattan distance heuristic
- Handles both grid-based and graph-based problems

## Usage
Run `A Star.py` with appropriate parameters for your pathfinding problem. 
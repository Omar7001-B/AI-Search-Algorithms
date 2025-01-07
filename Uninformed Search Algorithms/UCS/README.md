# Uniform Cost Search (UCS) Algorithm 💰

UCS is a graph search algorithm that finds the lowest-cost path between nodes in a weighted graph.

## How It Works
- Similar to BFS but uses priority queue
- Explores paths based on cumulative cost
- Always expands the lowest-cost path first
- Guarantees optimal solution in terms of path cost

## Features
- Complete: Will find solution if it exists
- Optimal for positive edge costs
- Time Complexity: O(b^(C*/ε)) where C* is optimal cost
- Space Complexity: O(b^(C*/ε))
- ε is minimum edge cost

## Implementation Details
- Uses Priority Queue for frontier
- Maintains path costs
- Implements path reconstruction
- Handles weighted graphs efficiently

## Usage
Run `UCS.py` with your weighted graph to find lowest-cost paths. 
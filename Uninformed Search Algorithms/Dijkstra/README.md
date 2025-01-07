# Dijkstra's Algorithm 🗺️

Dijkstra's algorithm finds the shortest paths between nodes in a weighted graph.

## How It Works
- Maintains set of unvisited nodes
- Continuously updates shortest distances
- Selects node with minimum distance
- Relaxes edges from selected node
- Similar to UCS but more efficient for shortest paths

## Features
- Complete for connected graphs
- Optimal for non-negative edge weights
- Time Complexity: O((V + E) log V) with priority queue
- Space Complexity: O(V)
- Can find paths to all nodes from source

## Implementation Details
- Uses Priority Queue for efficiency
- Maintains distance and predecessor arrays
- Implements path reconstruction
- Optimized for dense graphs
- Can handle both directed and undirected graphs

## Usage
Run `Dijkstra.py` with your weighted graph to find shortest paths from source to all nodes. 
# Iterative Deepening DFS (IDDFS) Algorithm 🔄

IDDFS combines the benefits of DFS and BFS by repeatedly running DLS with increasing depth limits.

## How It Works
- Starts with depth limit of 0
- Repeatedly runs DLS with increasing limits
- Continues until goal is found
- Combines space efficiency of DFS with completeness of BFS

## Features
- Complete: Will find solution if it exists
- Optimal for unweighted graphs
- Memory efficient like DFS
- Time Complexity: O(b^d) where d is solution depth
- Space Complexity: O(d)

## Implementation Details
- Uses DLS as subroutine
- Implements efficient depth tracking
- Avoids repeated states at same depth
- Perfect for unknown or infinite graphs

## Usage
Run `IDDFS.py` with your graph input to find optimal solutions with memory efficiency. 
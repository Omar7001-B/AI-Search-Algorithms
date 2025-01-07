# Depth-Limited Search (DLS) Algorithm 🎯

DLS is a variant of depth-first search that limits the maximum depth of exploration.

## How It Works
- Similar to DFS but with depth limit
- Stops exploration when depth limit is reached
- Returns failure if goal not found within limit
- Can be implemented recursively or iteratively

## Features
- Prevents infinite loops in infinite graphs
- Useful when solution depth is known
- Complete up to depth limit
- Time Complexity: O(b^l) where b is branching factor and l is limit
- Space Complexity: O(l)

## Implementation Details
- Uses depth counter
- Implements cutoff detection
- Returns special value for cutoff vs failure
- Good for game trees with known maximum depth

## Usage
Run `DLS.py` with your graph input and desired depth limit. 
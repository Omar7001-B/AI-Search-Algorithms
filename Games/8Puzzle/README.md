# 8-Puzzle Solver with A* Algorithm 🧩

An implementation of the 8-puzzle sliding tile game solver using the A* search algorithm.

## About the Puzzle
The 8-puzzle consists of 8 numbered tiles and one empty space. The goal is to rearrange the tiles to reach the target state:
```
1 2 3
4 5 6
7 8 _
```

## How to Use
1. Run `8 Puzzle (A_Star).py`
2. Input the initial state when prompted
3. The program will find the optimal solution path using A* search

## Algorithm Details
- Uses A* search algorithm for pathfinding
- Implements Manhattan distance heuristic
- Guarantees the shortest possible solution
- Visualizes the solution path step by step 
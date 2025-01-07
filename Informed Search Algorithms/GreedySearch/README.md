# Greedy Best-First Search Algorithm 🏃

Greedy Best-First Search is a heuristic search algorithm that makes locally optimal choices at each step.

## How It Works
- Uses only heuristic function h(n) to estimate distance to goal
- Always expands the node that appears closest to the goal
- Makes locally optimal choice at each step

## Features
- Very fast execution compared to other informed search algorithms
- Uses less memory than A*
- Good for problems where path optimality is not crucial
- Works well when heuristic accurately estimates distance to goal

## Trade-offs
- Does not guarantee optimal solution
- May get stuck in local optima
- Faster but less accurate than A*

## Usage
Run `Greedy Search.py` to see the algorithm in action on pathfinding problems. 
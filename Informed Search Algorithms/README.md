# Informed Search Algorithms 🔍

This directory contains implementations of various informed search algorithms. These algorithms use heuristic functions to guide the search process towards the goal state more efficiently than uninformed search methods.

## Available Algorithms

### 1. A* Search
- **Description**: A best-first search algorithm that combines path cost and heuristic estimation
- **Use Case**: Optimal pathfinding in various applications
- **Location**: `/A Star/`

### 2. Greedy Best-First Search
- **Description**: A heuristic search that always chooses the path that appears closest to the goal
- **Use Case**: Fast pathfinding when optimality is not crucial
- **Location**: `/GreedySearch/`

## Key Concepts
- All algorithms use heuristic functions to estimate the cost to the goal
- Heuristics must be admissible (never overestimate the actual cost)
- These algorithms are typically more efficient than uninformed search methods

## Common Applications
- Pathfinding in games and navigation
- Puzzle solving
- Route planning
- Resource allocation 
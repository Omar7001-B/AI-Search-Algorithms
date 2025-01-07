start_state = [1, 2, 3,
               0, 4, 6,
               7, 5, 8]

target = [1, 2, 3,
          4, 5, 6,
          7, 8, 0]

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
def apply_next_moves(state):
    all_next_states = []
    empty_index = state.index(0)
    for next_index in moves[empty_index]:
        new_state = state.copy()
        new_state[empty_index], new_state[next_index] = new_state[next_index], new_state[empty_index]
        all_next_states.append(new_state)
    return all_next_states

def f_cost(path):
    state = path[-1]
    g_cost = len(path)
    h_cost = sum(abs(state.index(i) % 3 - target.index(i) % 3) + abs(state.index(i) // 3 - target.index(i) // 3) for i in range(1, 9))
    return g_cost + h_cost

def a_star_8_puzzle(start):
    visited = []
    queue = [[start]]
    while queue:
        queue.sort(key=f_cost)
        path = queue.pop(0)
        state = path[-1]
        if state == target:
            return path
        if state not in visited:
            visited.append(state)
            for newState in apply_next_moves(state):
                queue.append(path + [newState])
    return None


def print_state(s):
    for i in range(0, 9, 3):
        print("| " + " | ".join(map(str, s[i:i+3])) + " |")
        print("-" * 13)

solution_path = a_star_8_puzzle(start_state)
if solution_path:
    print("Solution found:")
    for step, state in enumerate(solution_path):
        print(f"\nStep {step}:")
        print_state(state)
else:
    print("No solution found.")
"+"

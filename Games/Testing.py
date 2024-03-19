def f_cost(path, target):
    state = path[-1]
    g_cost = len(path)
    h_cost = sum(abs(state.index(i) % 3 - target.index(i) % 3) + abs(state.index(i) // 3 - target.index(i) // 3) for i in range(1, 9)) # Manhattan Distance
    return g_cost + h_cost


start_state = [1, 2, 3,
               0, 4, 6,
               7, 5, 8]

target = [1, 2, 3,
          4, 5, 6,
          7, 8, 0]

print(f_cost([start_state], target))

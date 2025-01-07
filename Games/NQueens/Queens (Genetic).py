import random


def calcPenalty(genome):
    visited = set()
    penalty = 0
    for idx, val in enumerate(genome):
        if (idx + val) in visited:
            penalty += 1
        if (idx - val) + 3 * len(genome) in visited:
            penalty += 1
        if val + 5 * len(genome) in visited:
            penalty += 1

        visited.add((idx - val) + 3 * len(genome))
        visited.add(idx + val)
        visited.add(val + 5 * len(genome))
    return penalty


# calcPenalty(queens)
def mutate(genome):
    idx1 = random.randint(0, len(genome) - 1)
    idx2 = random.randint(0, len(genome) - 1)
    newGenome = genome[:]
    newGenome[idx1], newGenome[idx2] = newGenome[idx2], newGenome[idx1]
    return newGenome


def mutate2(genome):
    idx = random.randint(0, len(genome) - 1)
    val = random.randint(0, len(genome) - 1)
    newGenome = genome[:]
    newGenome[idx] = val
    return newGenome


def crossover(genome1, genome2):
    splitIndex = random.randint(0, len(genome1) - 1)
    newGenome1 = genome1[:splitIndex] + genome2[splitIndex:]
    newGenome2 = genome2[:splitIndex] + genome1[splitIndex:]
    if random.random() < 0.5:
        return (newGenome1, newGenome2)
    if random.random() < 0.75:
        return (newGenome2, newGenome1, mutate(newGenome1), mutate(newGenome2))
    if random.random() < 0.9:
        return (newGenome1, newGenome1, mutate2(newGenome1), mutate2(newGenome2))
    return (newGenome1, newGenome2)


def main():
    population = [[random.randint(0, N - 1) for i in range(N)] for i in range(200)]
    while calcPenalty(population[0]):
        population.sort(key=calcPenalty)
        newPopulation = []
        idx = 0
        for _ in range(100):
            if idx >= len(population) - 10: break
            i = population.pop(idx)
            j = population.pop(idx + 1)
            newPopulation.extend(crossover(i, j))
            newPopulation.extend((i, j))
        population = newPopulation[:100]
    print(population[0], calcPenalty(population[0]))
    # newPopulation.extend(crossover(i,j))


if __name__ == "__main__":
    for N in range(8, 100):
        main()
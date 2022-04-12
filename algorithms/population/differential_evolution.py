from algorithms.initial_solution import get_initial_population
from algorithms.quality import quality
from algorithms.representation import get_number_of_bins
from copy import deepcopy
from random import sample

# TODO
POPULATION_SIZE = 0
ITERATIONS_COUNT = 0

# TODO: remove deepcopy from differential_evolution() if you do not need it.


def add(individual, vector):
    # TODO
    return None


def subtract(individual_a, individual_b):
    # TODO
    return None


def multiply(mutation_rate, difference):
    # TODO
    return None


def crossover(individual_a, individual_b):
    # TODO
    return None


def differential_evolution(items, mutation_rate):
    population = get_initial_population(items, POPULATION_SIZE)
    parents = None
    best = None
    current_best_list = []
    for _ in range(ITERATIONS_COUNT):
        current_best = None
        for i in range(len(population)):
            if parents is not None and quality(parents[i]) > quality(population[i]):
                population[i] = parents[i]
            if best is None or quality(population[i]) > quality(best):
                best = population[i]
            if current_best is None or quality(population[i]) > quality(current_best):
                current_best = population[i]
        current_best_list.append(get_number_of_bins(current_best))
        parents = population
        for i, parent in enumerate(parents):
            a, b, c = tuple(sample(parents[:i] + parents[i+1:], 3))
            d = add(a, multiply(mutation_rate, subtract(b, c)))
            population[i] = crossover(d, deepcopy(parent))
    return best, current_best_list

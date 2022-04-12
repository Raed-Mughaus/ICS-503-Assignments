from algorithms.initial_solution import get_initial_population
from algorithms.quality import *
from algorithms.representation import get_number_of_bins
from copy import deepcopy

#TODO: deepcopy makes your code slow. If you do not need it, remove it from the genetic_algorithm. It is called 4 times.

# TODO
POPULATION_SIZE = 2
ITERATIONS_COUNT = 10_000


def select_with_replacement(population, population_fitness):
    # TODO
    return None


def crossover(parent_a, parent_b, crossover_probability):
    # TODO
    return None, None


def mutate(individual, mutation_probability):
    #TODO
    return None


def genetic_algorithm(items, mutation_probability, crossover_probability):
    population = get_initial_population(items, POPULATION_SIZE)
    best = None
    current_best_list = []
    for i in range(ITERATIONS_COUNT):
        population_fitness = population_quality(population)
        current_best = None
        for j, individual in enumerate(population):
            individual_quality = population_fitness[j]
            if best is None or individual_quality > quality(best):
                best = individual
            if current_best is None or individual_quality > quality(current_best):
                current_best = individual
        current_best_list.append(get_number_of_bins(current_best))
        q = []
        for _ in range(POPULATION_SIZE // 2):
            parent_a = select_with_replacement(population, population_fitness)
            parent_b = select_with_replacement(population, population_fitness)
            child_a, child_b = crossover(deepcopy(parent_a), deepcopy(parent_b), crossover_probability)
            q.append(
                mutate(deepcopy(child_a), mutation_probability)
            )
            q.append(
                mutate(deepcopy(child_b), mutation_probability)
            )
        population = q
    return best, current_best_list

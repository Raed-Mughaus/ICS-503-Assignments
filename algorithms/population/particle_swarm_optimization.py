from algorithms.initial_solution import get_initial_population
from algorithms.quality import quality
from algorithms.representation import get_number_of_bins
from random import sample
from collections import namedtuple
from numpy.random import random as rand_vec

SWARM_SIZE = 0
NEIGHBORHOOD_SIZE = 0
ITERATIONS_COUNT = 0
VECTOR_LENGTH = 1000
VELOCITY_PROPORTION = 0
PERSONAL_BEST_PROPORTION = 0
INFORMANTS_BEST_PROPORTION = 0
GLOBAL_BEST_PROPORTION = 0
JUMP_SIZE = 0


def random_initial_velocity():
    # TODO: return a numpy vector
    return None


def add_4(vector_a, vector_b, vector_c, vector_d):
    # TODO
    return None


def add_2(individual, vector):
    # TODO
    return None


def subtract(individual_a, individual_b):
    # TODO
    return None


def multiply_val_by_vec(proportion_value, vector):
    # TODO
    return None


def multiply_vec_by_vec(proportion_vector, vector):
    # TODO
    return None


def particle_swarm_optimization(items):
    population = get_initial_population(items, SWARM_SIZE)
    velocities = [
        random_initial_velocity()
        for _ in range(SWARM_SIZE)
    ]
    BestRecord = namedtuple('BestRecord', 'individual quality')
    best_records = [
        BestRecord(individual, quality(individual))
        for individual in population
    ]
    current_best_list = []
    for _ in range(ITERATIONS_COUNT):
        for i, individual in enumerate(population):
            personal_best = best_records[i]
            informants = sample(best_records, NEIGHBORHOOD_SIZE)
            informants_best = max(informants, key=lambda record: record.quality)
            global_best = max(best_records, key=lambda record: record.quality)

            b = PERSONAL_BEST_PROPORTION * rand_vec(VECTOR_LENGTH)
            c = INFORMANTS_BEST_PROPORTION * rand_vec(VECTOR_LENGTH)
            d = GLOBAL_BEST_PROPORTION * rand_vec(VECTOR_LENGTH)

            velocities[i] = add_4(
                multiply_val_by_vec(VELOCITY_PROPORTION, velocities),
                multiply_vec_by_vec(b, subtract(personal_best, individual)),
                multiply_vec_by_vec(c, subtract(informants_best, individual)),
                multiply_vec_by_vec(d, subtract(global_best, individual)),
            )
        for i, individual in enumerate(population):
            population[i] = add_2(
                individual,
                multiply_val_by_vec(JUMP_SIZE, velocities[i])
            )
        current_best_quality = -float('inf')
        current_best_bins_count = None
        for i in range(len(population)):
            individual_quality = quality(population[i])
            if individual_quality > best_records[i].quality:
                best_records[i] = BestRecord(population[i], individual_quality)
            if individual_quality > current_best_quality:
                current_best_quality = individual_quality
                current_best_bins_count = get_number_of_bins(population[i])
        current_best_list.append(current_best_bins_count)
    global_best = max(best_records, key=lambda record: record.quality)
    return global_best.individual, current_best_list

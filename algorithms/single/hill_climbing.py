from algorithms.initial_solution import get_initial_solution
from algorithms.tweak import tweak
from algorithms.quality import quality
from algorithms.representation import get_number_of_bins


# TODO, for algorithms with a single loop, e.g. hill climbing
ITERATIONS_COUNT = 0

# TODO, for algorithms with 2 loops, e.g. steepest ascent hill climbing
OUTER_ITERATIONS_COUNT = 0
INNER_ITERATIONS_COUNT = 0

HC_WITH_RANDOM_RESTARTS_T_INTERVALS = []


def hill_climbing(items):
    s = get_initial_solution(items)
    current_best_list = []
    for i in range(ITERATIONS_COUNT):
        r = tweak(s)
        if quality(r) > quality(s):
            s = r
        current_best_list.append(get_number_of_bins(s))
    return s, current_best_list


def steepest_ascent_hill_climbing(items):
    s = get_initial_solution(items)
    current_best_list = []
    for _ in range(OUTER_ITERATIONS_COUNT):
        r = tweak(s)
        for _ in range(INNER_ITERATIONS_COUNT - 1):
            w = tweak(s)
            if quality(w) > quality(r):
                r = w
        if quality(r) > quality(s):
            s = r
        current_best_list.append(get_number_of_bins(s))
    return s, current_best_list


def steepest_ascent_hill_climbing_with_replacement(items):
    s = get_initial_solution(items)
    best = s
    current_best_list = []
    for _ in range(OUTER_ITERATIONS_COUNT):
        r = tweak(s)
        for _ in range(INNER_ITERATIONS_COUNT - 1):
            w = tweak(s)
            if quality(w) > quality(r):
                r = w
        s = r
        if quality(s) > quality(best):
            best = s
        current_best_list.append(get_number_of_bins(s))
    return best, current_best_list


def hill_climbing_with_random_restarts(items):
    t = HC_WITH_RANDOM_RESTARTS_T_INTERVALS
    s = get_initial_solution(items)
    best = s
    current_best_list = []
    for iterations_count in t:
        for _ in range(iterations_count):
            r = tweak(s)
            if quality(r) > quality(s):
                s = r
            current_best_list.append(get_number_of_bins(s))
        if quality(s) > quality(best):
            best = s
        s = get_initial_solution(items)
    return best, current_best_list

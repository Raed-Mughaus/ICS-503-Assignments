from random import random
from math import exp


# TODO, for algorithms with a single loop, e.g. hill climbing
ITERATIONS_COUNT = 0

# TODO, for algorithms with 2 loops, e.g. steepest ascent hill climbing
OUTER_ITERATIONS_COUNT = 0
INNER_ITERATIONS_COUNT = 0

# TODO
HC_WITH_RANDOM_RESTARTS_T_INTERVALS = []

# TODO
ITERATED_LOCAL_SEARCH_T_INTERVALS = []


def get_initial_solution(items):
    # TODO
    pass


def tweak(s):
    # Note: take tabu_search into consideration when implementing this method. MAYBE you want your solution to include
    # a description of the tweak. For example, maybe you want to return something like:
    # ("move item x from bin y to z", tweaked_s)
    # TODO
    pass


def quality(s):
    # TODO
    pass


def get_number_of_bins(s):
    # TODO
    pass


def is_tabu(s, tabu_list):
    # TODO
    pass


def enqueue_into_tabu_list(s, tabu_list):
    # TODO
    pass


def perturb(s):
    # TODO
    pass


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


def simulated_annealing(t, decrease_t, items=None, initial_solution=None, iterations_count=ITERATIONS_COUNT):
    assert (items is None) != (initial_solution is None)
    s = get_initial_solution(items) if items is not None else initial_solution
    best = s
    current_best_list = []
    for _ in range(iterations_count):
        r = tweak(s)
        r_quality = quality(r)
        s_quality = quality(s)
        if r_quality > s_quality or random() < exp((r_quality - s_quality) / t):
            s = r
        t = decrease_t(t)
        if quality(s) > quality(best):
            best = s
        current_best_list.append(get_number_of_bins(s))
        if t <= 0:
            break
    return best, current_best_list


def tabu_search(
        tabu_list_capacity, items=None, initial_solution=None,
        iterations_count=OUTER_ITERATIONS_COUNT * INNER_ITERATIONS_COUNT
):
    assert (items is None) != (initial_solution is None)
    s = get_initial_solution(items) if items is not None else initial_solution
    best = s
    current_best_list = []
    tabu_list = []
    enqueue_into_tabu_list(s, tabu_list)
    outer_iterations_count = max(1, int(round(iterations_count / INNER_ITERATIONS_COUNT)))
    for _ in range(outer_iterations_count):
        if len(tabu_list) > tabu_list_capacity:
            tabu_list.pop(0)
        r = tweak(s)
        for _ in range(INNER_ITERATIONS_COUNT - 1):
            w = tweak(s)
            if not is_tabu(w, tabu_list) and (quality(w) > quality(r) or is_tabu(r, tabu_list)):
                r = w
        if not is_tabu(r, tabu_list):
            s = r
            enqueue_into_tabu_list(r, tabu_list)
        if quality(s) > quality(best):
            best = s
        current_best_list.append(get_number_of_bins(s))
    return best, current_best_list


def iterated_local_search(local_search, items=None, initial_solution=None):
    t = ITERATED_LOCAL_SEARCH_T_INTERVALS
    current_best_list = []
    assert (items is None) != (initial_solution is None)
    s = get_initial_solution(items) if items is not None else initial_solution
    h = s
    best = s
    for iterations_count in t:
        s, local_current_best_list = local_search(s, iterations_count)
        current_best_list += local_current_best_list
        if quality(s) > quality(best):
            best = s
        h = s if quality(s) >= quality(h) else h
        s = perturb(h)
    return best, current_best_list


def iterated_simulated_annealing(initial_temperature, decrease_t, items=None, initial_solution=None):
    return iterated_local_search(
        lambda s, iterations_count: simulated_annealing(
            initial_temperature,
            decrease_t,
            initial_solution=s,
            iterations_count=iterations_count,
        ),
        items=items,
        initial_solution=initial_solution,
    )


def iterated_tabu_search(tabu_list_capacity, items=None, initial_solution=None):
    return iterated_local_search(
        lambda s, iterations_count: tabu_search(
            tabu_list_capacity,
            initial_solution=s,
            iterations_count=iterations_count,
        ),
        items=items,
        initial_solution=initial_solution,
    )

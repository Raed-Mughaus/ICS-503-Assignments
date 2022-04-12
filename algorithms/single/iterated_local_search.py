from algorithms.single.simulated_annealing import simulated_annealing
from algorithms.single.tabu_search import tabu_search
from algorithms.initial_solution import get_initial_solution
from algorithms.quality import quality


# TODO
ITERATED_LOCAL_SEARCH_T_INTERVALS = []


def perturb(s):
    # TODO
    pass


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

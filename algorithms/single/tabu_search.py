from algorithms.initial_solution import get_initial_solution
from algorithms.tweak import tweak
from algorithms.quality import quality
from algorithms.representation import get_number_of_bins


# TODO, for algorithms with 2 loops, e.g. steepest ascent hill climbing
OUTER_ITERATIONS_COUNT = 0
INNER_ITERATIONS_COUNT = 0


def is_tabu(s, tabu_list):
    # TODO
    pass


def enqueue_into_tabu_list(s, tabu_list):
    # TODO
    pass


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

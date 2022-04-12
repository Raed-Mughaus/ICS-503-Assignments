from algorithms.initial_solution import get_initial_solution
from algorithms.tweak import tweak
from algorithms.quality import quality
from algorithms.representation import get_number_of_bins
from random import random
from math import exp


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

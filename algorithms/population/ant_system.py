from algorithms.quality import quality
from algorithms.representation import get_number_of_bins

POPULATION_SIZE = 0
ITERATIONS_COUNT = 0
EVAPORATION = 0
INITIAL_PHEROMONES = 0


def get_components(items):
    # TODO
    return None


def get_legal_components_indices(solution, components):
    # TODO
    return None  # Return a list of indices


def create_empty_solution():
    # TODO
    return None


def is_complete(solution):
    # TODO
    return None  # return True or false


def select_component(components, pheromones):
    # TODO
    return None


def update_pheromone(pheromone, solution):
    # TODO
    return None  # return the new pheromone


def add_component_to_solution(component, solution):
    # TODO
    pass


def is_component_used_in_solution(component, solution):
    # TODO
    return None  # True or False


def ant_system(items):
    components = get_components(items)
    pheromones = [
        INITIAL_PHEROMONES
        for _ in range(len(components))
    ]
    best = None
    current_best_list = []
    for _ in range(ITERATIONS_COUNT):
        population = []
        current_best = None
        for _ in range(POPULATION_SIZE):
            solution = create_empty_solution()
            while not is_complete(solution):
                legal_components_indices = get_legal_components_indices(solution, components)
                legal_components = [components[i] for i in legal_components_indices]
                legal_components_pheromones = [pheromones[i] for i in legal_components_indices]
                component = select_component(legal_components, legal_components_pheromones)
                add_component_to_solution(component, solution)
            solution_quality = quality(solution)
            if best is None or solution_quality > quality(best):
                best = solution
            if current_best is None or solution_quality > quality(current_best):
                current_best = solution
            population.append(solution)
        current_best_list.append(get_number_of_bins(current_best))
        for i in range(len(pheromones)):
            pheromones[i] *= (1 - EVAPORATION)
        for solution in population:
            for i, component in enumerate(components):
                if is_component_used_in_solution(component, solution):
                    pheromones[i] = update_pheromone(pheromones[i], solution)
    return best, current_best_list

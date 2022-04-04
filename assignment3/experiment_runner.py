from os.path import isdir
from pathlib import Path
from assignment3.report.data_generator import generate_data
from assignment3.report.plots_generator import generate_plots, generate_final_plots
from assignment3.report.report_generator import generate_report
from assignment3.report.algorithm import *


INSTANCES_INDICES = range(10)
RUNS_COUNT = 10  # must be at least 2

ALGORITHMS = [

    # Use importable to import previous experiment results
    # Importable(
    #     'Hill-climbing', # your previously provided algorithm name
    #     'HC', # your previously provided instance name
    #     experiment_number=AN_INTEGER,
    # ),

    # Use runnable to run an algorithm
    # Runnable(
    #     'Genetic Algorithm',
    #     'GA M-1.0 C-1.0',
    #     lambda items: genetic_algorithm(items, YOUR_MUTATION_PROBABILITY, YOUR_CROSSOVER_PROBABILITY),
    # ),
]


def load_instances():
    bin_items = pd.read_csv('Bin Items.csv')
    return [
        [
            item_size
            for item_size in bin_items[f'Instance {i}']
        ]
        for i in range(1, 11)
    ]


def find_experiment_number():
    i = 0
    while True:
        i += 1
        if not isdir(f'experiments/Experiment {i}'):
            break
    return i


algorithm_name_to_instances = {
    algorithm.name: []
    for algorithm in ALGORITHMS
}
for algorithm in ALGORITHMS:
    algorithm_name_to_instances[algorithm.name].append(algorithm.instance)

instances = load_instances()
experiment_number = find_experiment_number()
Path(f'experiments/Experiment {experiment_number}')\
    .mkdir(parents=True, exist_ok=True)
generate_data(instances, experiment_number, ALGORITHMS, INSTANCES_INDICES, runs_count=RUNS_COUNT)
print("Generating plots...")
generate_plots(experiment_number, algorithm_name_to_instances, INSTANCES_INDICES)
generate_final_plots(experiment_number, ALGORITHMS, INSTANCES_INDICES)
print("Plots generated")
print("Generating report...")
generate_report(experiment_number, algorithm_name_to_instances, INSTANCES_INDICES)
print("Report generated")

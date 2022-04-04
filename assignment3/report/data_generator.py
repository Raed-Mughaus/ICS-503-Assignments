from assignment3.report.experiment_files import *
from pathlib import Path
import pandas as pd
from tqdm import tqdm


def _mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_to_csv(data, path):
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(path, header=False, index=False)


def find_best_so_far_list(current_best_list):
    best_so_far_list = [current_best_list[0]]
    for current_best in current_best_list[1:]:
        best_so_far = min(best_so_far_list[-1], current_best)
        best_so_far_list.append(best_so_far)
    return best_so_far_list


def generate_data(instances, experiment_number, algorithms, instances_indices, runs_count=10):
    for algorithm in algorithms:
        t = tqdm(instances_indices, f'{algorithm.name} - {algorithm.instance}')
        for instance_idx in t:
            items = instances[instance_idx]
            best_so_far_result = {}
            current_best_result = {}
            for i in range(runs_count):
                t.set_postfix({'Instance': instance_idx, 'Run': i})
                algorithm_result, current_best_list = algorithm(instance_idx+1, i, items)
                current_best_result[f'{i}'] = current_best_list
                best_so_far_result[f'{i}'] = find_best_so_far_list(current_best_list)
            data_path = f'{get_data_path(experiment_number, instance_idx + 1, algorithm.name)}/{algorithm.instance}/'
            _mkdir(data_path)
            write_to_csv(best_so_far_result, f'{data_path}/Best so far.csv')
            if len(current_best_result) != 0:
                write_to_csv(current_best_result, f'{data_path}/Current best.csv')

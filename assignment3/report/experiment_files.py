

def get_instance_path(experiment_number, instance_number):
    return f'experiments/Experiment {experiment_number}/Instance {instance_number}'


def get_data_path(experiment_number, instance_number, algorithm_name):
    return f'{get_instance_path(experiment_number, instance_number)}/data/{algorithm_name}'


def get_plots_path(experiment_number, instance_number, algorithm_name=None):
    if algorithm_name is None:
        return f'{get_instance_path(experiment_number, instance_number)}/plots'
    else:
        return f'{get_instance_path(experiment_number, instance_number)}/plots/{algorithm_name}'

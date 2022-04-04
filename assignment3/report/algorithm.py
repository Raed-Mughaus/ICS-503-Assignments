import pandas as pd
from assignment3.report.experiment_files import get_data_path


class Algorithm:

    def __init__(self, name, instance):
        self.name = name
        self.instance = instance


class Importable(Algorithm):

    def __init__(self, name, instance, experiment_number):
        super().__init__(name, instance)
        self.experiment_number = experiment_number

    def __call__(self, instance_number, run_idx, items):
        data_path = get_data_path(self.experiment_number, instance_number, self.name)
        file_path = f'{data_path}/{self.instance}/Current best.csv'
        current_best = pd.read_csv(file_path, header=None, index_col=None).iloc[:, run_idx]
        return None, current_best


class Runnable(Algorithm):

    def __init__(self, algorithm_name, algorithm_instance, fn):
        super().__init__(algorithm_name, algorithm_instance)
        self.fn = fn

    def __call__(self, instance_number, run_idx, items):
        return self.fn(items)

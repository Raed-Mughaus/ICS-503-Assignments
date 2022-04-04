from pathlib import Path
from report.utils import *
from report.experiment_files import *
from matplotlib.pyplot import figure
import pandas as pd


def _get_final_result(data_path):
    data = pd.read_csv(f'{data_path}/Best so far.csv', header=None, index_col=None)
    return data.iloc[len(data) - 1]


def _generate_box_and_ci_plots_for_an_algorithm(data_path, plots_path, algorithm_instances):
    data_frame = pd.DataFrame({
        algorithm_instance: _get_final_result(f'{data_path}/{algorithm_instance}')
        for algorithm_instance in algorithm_instances
    })
    figure(figsize=(10, 5.5), dpi=80)
    data_frame.boxplot(showmeans=True)
    plt.title('Box Plots')
    plt.savefig(f'{plots_path}/Box Plots.png')
    plt.close()

    figure(figsize=(10, 5.5), dpi=80)
    for i in range(len(data_frame.columns)):
        column = data_frame.columns[i]
        plot_confidence_interval(i + 1, data_frame[column])
    plt.xticks(range(1, len(data_frame.columns) + 1), data_frame.columns)
    plt.grid()
    plt.title('Confidence Intervals')
    plt.savefig(f'{plots_path}/Confidence Intervals.png')
    plt.close()


def _generate_box_and_ci_plots_for_all_algorithms(experiment_number, instance_number, algorithms):
    plots_path = get_plots_path(experiment_number, instance_number)
    data_frame = pd.DataFrame({
        algorithm.instance: _get_final_result(f'{get_data_path(experiment_number, instance_number, algorithm.name)}/{algorithm.instance}')
        for algorithm in algorithms
    })
    figure(figsize=(10, 6.5), dpi=80)
    data_frame.boxplot(showmeans=True)
    plt.xticks(rotation=30)
    plt.title('Box Plots')
    plt.savefig(f'{plots_path}/Box Plots.png')
    plt.close()

    figure(figsize=(10, 6.5), dpi=80)
    for i in range(len(data_frame.columns)):
        column = data_frame.columns[i]
        plot_confidence_interval(i + 1, data_frame[column])
    plt.xticks(range(1, len(data_frame.columns) + 1), data_frame.columns, rotation=30)
    plt.grid()
    plt.title('Confidence Intervals')
    plt.savefig(f'{plots_path}/Confidence Intervals.png')
    plt.close()


def _generate_avg_and_ci_plot(data_path, plots_path, algorithm_instance, file_name, title, subtitle):
    file_path = f'{data_path}/{algorithm_instance}/{file_name}.csv'
    data = pd.read_csv(file_path, index_col=None, header=None)
    ci_step = max(1, len(data) // 10)
    figure(figsize=(6.4, 3.8), dpi=80)

    plt.plot(data.mean(axis=1), color='green')

    for i in range(10):
        iteration = i * ci_step
        bin_count_list = data.iloc[iteration].values.tolist()
        plot_confidence_interval(iteration, bin_count_list, horizontal_line_width=len(data)/20)

    plt.title(title)
    plt.suptitle(subtitle)
    plt.xlabel('Iterations')
    plt.ylabel('Bins count')
    plt.xticks(range(0, len(data) + 1, ci_step))
    plt.grid()
    Path(f'{plots_path}/{algorithm_instance}/').mkdir(parents=True, exist_ok=True)
    plt.savefig(f'{plots_path}/{algorithm_instance}/{file_name}.png')
    plt.close()


def _generate_plots_for_algorithm(experiment_number, algorithm_name, algorithm_instances, instances_indices):
    for instance_idx in instances_indices:
        instance_number = instance_idx + 1
        data_path = get_data_path(experiment_number, instance_number, algorithm_name)
        plots_path = get_plots_path(experiment_number, instance_number, algorithm_name)
        for algorithm_instance in algorithm_instances:
            _generate_avg_and_ci_plot(data_path, plots_path, algorithm_instance, 'Best so far', 'Best so far', algorithm_instance)
            _generate_avg_and_ci_plot(data_path, plots_path, algorithm_instance, 'Current best', 'Current best', algorithm_instance)
        _generate_box_and_ci_plots_for_an_algorithm(data_path, plots_path, algorithm_instances)


def generate_plots(experiment_number, algorithm_name_to_instances, instances_indices):
    for algorithm_name, algorithms_instances in algorithm_name_to_instances.items():
        _generate_plots_for_algorithm(
            experiment_number,
            algorithm_name,
            algorithms_instances,
            instances_indices,
        )


def generate_final_plots(experiment_number, algorithms, instances_indices):
    for instance_idx in instances_indices:
        _generate_box_and_ci_plots_for_all_algorithms(experiment_number, instance_idx + 1, algorithms)

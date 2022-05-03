import matplotlib.pyplot as plt
import statistics
from math import sqrt


def get_descriptive_statistics(values, z=1.96):
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    confidence_interval = z * stdev / sqrt(len(values))
    median = statistics.median(values)
    return mean, stdev, median, confidence_interval


def plot_confidence_interval(x, values, z=1.96, color='blue', horizontal_line_width=0.25):
    mean, stdev, _, confidence_interval = get_descriptive_statistics(values, z)
    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color='red')

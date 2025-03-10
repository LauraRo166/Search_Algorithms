import pandas as pd
import matplotlib.pyplot as plt
from utils.execution_time_gathering import gather_execution_times

def plot_execution_times(df):
    """
    Plots the execution times of the search algorithms.

    :param df: DataFrame with the execution times.
    """
    plt.figure(figsize=(12, 8))

    for algorithm in ['Linear Search', 'Binary Search', 'Ternary Search']:
        if algorithm in df.columns:
            plt.plot(df['Size'], df[algorithm], label=algorithm)

    plt.xlabel('Input size')
    plt.ylabel('Execution time (seconds)')
    plt.title('Analysis of execution times of search algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    min_size = 10_000
    max_size = 1_000_000
    step = 50_000
    samples_per_size = 10
    df = gather_execution_times(min_size, max_size, step, samples_per_size)
    plot_execution_times(df)

if __name__ == '__main__':
    main()

import pandas as pd
import matplotlib.pyplot as plt
from utils.execution_time_gathering import gather_execution_times

def plot_execution_times(df):
    """
    Grafica los tiempos de ejecución de los algoritmos de búsqueda.

    :param df: DataFrame con los tiempos de ejecución.
    """
    plt.figure(figsize=(12, 8))

    for algorithm in ['LinearSearch', 'BinarySearch', 'TernarySearch']:
        if algorithm in df.columns:
            plt.plot(df['Size'], df[algorithm], label=algorithm)

    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Análisis de tiempos de ejecución de algoritmos de búsqueda')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Parámetros
    min_size = 10_000
    max_size = 1_000_000
    step = 50_000
    samples_per_size = 10

    # Recolectar tiempos de ejecución
    df = gather_execution_times(min_size, max_size, step, samples_per_size)

    # Graficar tiempos de ejecución
    plot_execution_times(df)

if __name__ == '__main__':
    main()

"""
CS1 22fa MP5 Part C

Student Name: Julian Navarro

Brief Overview: This program plots a graph of the frequency of the pokemon
types in the 'pokedex.csv' file. This graph is a bar chart.

Data Source(s): pokedex.csv
Data Science Question: What is the most popular type of the first 151 pokemon?

Room for Improvement: (Optional)
"""

import matplotlib.pyplot as plt
import csv
import os
# You may add additional imports if you choose to use them

# You may choose to change/add constants here as appropriate for
# your plotting program.

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


def collect_pokemon_type(filename):
    """
    Function takes a string csv filename 'filename' and stores the
    'type' column of the pokemon in a list that is returned.

    Arguments:
        -'filename' (string): Name of the csv file

    Returns:
        -lst: Returns a list of the type colunm of all the pokemon
        in the csv file 'filename'.
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        lst = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                lst.append(row['type'])
        return lst


def type_freq(lst_type):
    """
    Function takes a list 'lst_type' and returns a tuple with two
    lists as arguments. This lists consist of all the possible type
    of pokemon (non repeated) and the frequency in which the types
    are repeated.

    Arguments:
        - 'lst_type' (lst): List of all the types of the pokemons

    Returns:
        - (lst, lst): Returns a tuple of two lists that hold the types
        of the pokemon and the frequency of their repetitiveness.
    """
    types = []
    frequency = []
    for i in lst_type:
        if i not in types:
            types.append(i)
            count = lst_type.count(i)
            frequency.append(count)
    return (types, frequency)


def plot_type(ax):
    """
    Plots the pokemon type data on the provided `ax`, creating a bar graph
    with the pokemon types on the x axis and the frequency of them in
    the y axis.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    lst_type = collect_pokemon_type('pokedex.csv')
    types, freq = type_freq(lst_type)
    type_colors = ['green', 'coral', 'blue', 'skyblue', 'grey', 'purple',
                   'yellow', 'darkgoldenrod', 'pink', 'olive', 'red',
                   'magenta', 'burlywood', 'silver', 'indigo', 'turquoise',
                   'royalblue']
    ax.bar(types, freq, color=type_colors, width=0.6)
    ax.set_xticklabels(types, rotation=45)
    ax.set_xlabel('Pokemon Types')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of the Pokemon Types')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of the pokemon types based on pokedex.csv.

    Arguments:
        -None

    Returns:
        -None
    """
    # Provided as a start for Part C, modify as needed
    fig, ax = plt.subplots()

    plot_type(ax)

    # Recommended: But you would need to change based on your
    # plot programming. Remove if you don't use this.
    # configure_plot(ax)
    fig.set_size_inches(8, 8)
    plt.show()


if __name__ == '__main__':
    start()

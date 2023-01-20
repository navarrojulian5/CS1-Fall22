"""
CS1 22fa MP5 Part A
Starter Code

Student Name: Julian Navarro
"""
import numpy as np
import matplotlib.pyplot as plt
import math

GRAVITY = 9.81          # m/s^2
ANGLE_OF_LAUNCH = 45    # in degrees from horizon
INITIAL_VELOCITY = 150  # m/s

# Constants for plotting the single trajectory
# Note: We could use offset factors (e.g. 5%) here to generalize the
# label positioning large vs. small distances, but to make it easier
# to test without floating point subtleties, we will use constants
X_LABEL_OFFSET = 150
Y_LABEL_OFFSET = 10

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


# Exercise A.1.
def calculate_velocity():
    """
    Function takes no argument and returns the x and y velocities corresponding
    to a initial velocity.

    Arguments:
        -None

    Returns:
        tuple(float, float) - Represents the velocity vector of vxi and vyi
    """
    rad = math.radians(ANGLE_OF_LAUNCH)
    x_vector = INITIAL_VELOCITY * math.cos(rad)
    y_vector = INITIAL_VELOCITY * math.sin(rad)
    return (x_vector, y_vector)


# Exercise A.2.
def calculate_position(dt):
    """
    Functions takes a time 'dt' and returns a tuple corresponding to the
    position of the rocket.

    Arguments:
        - dt (int): Represents the time elapsed

    Returns:
        - (tuple): (x,y) position of the rocket at 'dt'
    """
    (X0, Y0) = (0, 0)
    x_velocity, y_velocity = calculate_velocity()
    x_position = x_velocity * dt + X0
    y_position = y_velocity * dt - 0.5 * GRAVITY * math.pow(dt, 2) + Y0
    position = (x_position, y_position)
    return position


# Exercise A.3.
def flight_time():
    """
    Function takes no argument and returns the total flight time of a rocket

    Arguments:
        -None

    Returns:
        - (float): Total flight time of a rocket.
    """
    x_velocity, y_velocity = calculate_velocity()
    time = 2 * y_velocity / GRAVITY
    return time


# Exercise A.4.
def generate_rocket_positions(tof):
    """
    Given a total time 'tof', function returns a data of the positions
    of the rocket. We assume that the initial position of the
    rocket is (0,0)

    Arguments:
        - 'tof' (int): Total flight time of the rocket.

    Returns:
        - tuple[lst[int]] - Returns tuple with a list of positions of a rocket.
    """
    xs = []
    ys = []
    for i in np.arange(0, tof, 0.1):
        px, py = calculate_position(i)
        xs.append(px)
        ys.append(py)

    # Handles the last coordinate case when y == 0.0 (rocket hits ground)
    if ys[-1] != 0.0:
        px, py = calculate_position(tof)
        xs.append(px)
        ys.append(py)
    return (xs, ys)


# Exercise: A.5.
def plot_labels(highest_pt, landing_pt, line_color, ax):
    """
    Plots the points of interest on the `ax` with annotated labels
    for each point, sharing the passed `line_color`.

    Arguments:
        - highest_point (int/float, int/float): (x, y) of launch peak
        - landing_pt (int/float, int/float): (x, y) of landing point
        - line_color (str): line color for labels to share with a plotted line
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # (1146.788990825688, 573.3944954128439)
    (half_dist, max_y) = highest_pt
    # (2293.577981651376, 0.0)
    (total_dist, last_y) = landing_pt

    # Plot max height marker/label
    # '573m'
    maxh_label = f'{max_y:.0f}m'
    # '(1296.788990825688, 583.3944954128439)'
    maxh_label_coords = (half_dist + X_LABEL_OFFSET,
                         max_y + Y_LABEL_OFFSET)

    # Make sure you can reason about what these next statements do
    ax.annotate(maxh_label, xy=highest_pt, xytext=maxh_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(half_dist, max_y, marker='D', color=line_color,
            markersize=MARKER_SIZE)

    # Next, we plot the label marking the total distance traveled
    # (when the rocket lands)

    # '2294m'
    dist_label = f'{total_dist:.0f}m'
    # '(996.788990825688, 10)'
    dist_label_coords = (total_dist - X_LABEL_OFFSET,
                         Y_LABEL_OFFSET)

    ax.annotate(dist_label, xy=landing_pt, xytext=dist_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(total_dist, last_y, marker='*', color=line_color,
            markersize=MARKER_SIZE)


# Exercise A.6.
def plot_launch(ax):
    """
    Plots the launch data on the provided `ax`, creating a trajectory
    line graph with two plotted points of interest (max height and total
    distance traveled). Also sets up the legend for the plot, including
    the trajectory line and markers for the max height and landing points.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # Generate the x/y values for the line
    tof = flight_time()
    (xs, ys) = generate_rocket_positions(tof)

    # The highest point is exactly mid-launch
    highest_pt = calculate_position(tof / 2)

    # The rocket lands at the last (x, y) position
    landing_pt = (xs[-1], ys[-1])

    legend_label = f'Launch Trajectory ({tof:.1f}s)'

    lines = ax.plot(xs, ys, 'ro', markersize=MARKER_SIZE,
                    linewidth=LINE_WIDTH, label=legend_label)

    # The rest of the code below should be unmodified

    # Get the line color of the plotted line (lines is a list
    # of all lines plotted above, but we only have one)
    line_color = lines[0].get_color()

    # Pass the two points of interest to plot the labelled
    # points sharing the same line color as the line,
    # and passing the required Axes which contains state
    # and methods for the plot we've been modifying
    plot_labels(highest_pt, landing_pt, line_color, ax)


# Provided
def configure_plot(ax):
    """
    Configures the settings of the `ax` plot, including
    setting up the legend for the markers, defining the x and y
    axis bounds and labels, and the title of the plot.
    """
    # A bit of a hack, but add the marker symbols to the legend
    # without adding a legend item for each plotted marker
    # Note: 'k' is the shorthand for black ('b' is blue)
    ax.plot([], [], 'k*', label='Max Distance', markersize=MARKER_SIZE)
    ax.plot([], [], 'kD', label='Max Height', markersize=MARKER_SIZE)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.legend(loc='upper left')
    X_BOUND_OFFSET = 100
    Y_BOUND_OFFSET = 100
    xbounds = ax.get_xbound()
    ybounds = ax.get_ybound()
    ax.set_xlim(xbounds[0] - X_BOUND_OFFSET, xbounds[-1] + X_BOUND_OFFSET)
    ax.set_ylim(ybounds[0], ybounds[-1] + (Y_BOUND_OFFSET))

    ax.set_title('Bottle Rocket Launch: Trajectory on Earth')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of the test launch data using this
    program's constants for an example initial velocity, angle, and gravity
    rate.
    """
    fig, ax = plt.subplots()
    plot_launch(ax)
    configure_plot(ax)
    fig.set_size_inches(8, 8)
    plt.show()


if __name__ == '__main__':
    start()

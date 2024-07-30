import numpy as np
import matplotlib.pyplot as plt
import math

def circ(x, y):
    return x ** 2 + y ** 2

def sml_circ(x, y):
    theta = np.arctan2(y, x)
    return np.where((theta >= 0) & (theta <= 2), x ** 2 + y ** 2, np.nan)

def rad1(x, y):
    return np.where((x <= 0) & (x >= np.cos(2)), np.tan(2) * x - y, np.nan)

def rad2(x, y):
    return np.where((x <= 1) & (x >= 0), y, np.nan)

color_pool = ["blue", "olive", "blue", "blue", "lime", "slategrey", "hotpink"]

def plot_implicit_functions(functions, title, contours, labels, x_interval, y_interval, graph_name, font_size, delicacy=int(1e3)):
    colors = color_pool[:len(contours)]
    # See https://matplotlib.org/stable/gallery/color/named_colors.html

    def make_grid(alpha, beta):
        try:
            return np.meshgrid(alpha, beta)
        except np.core._exceptions._ArrayMemoryError:
            alpha_midpoint = (alpha[0] + alpha[1]) / 2
            beta_midpoint = (beta[0] + beta[1]) / 2
            grid_a = make_grid((alpha[0], alpha_midpoint), (beta[0], beta_midpoint))
            grid_b = make_grid((alpha_midpoint, alpha[1]), (beta[0], beta_midpoint))
            grid_c = make_grid((alpha_midpoint, alpha[1]), (beta_midpoint, beta[1]))
            grid_d = make_grid((alpha[0], alpha_midpoint), (beta_midpoint, beta[1]))
            return grid_a[0]+grid_b[0]+grid_c[0]+grid_d[0], grid_a[1]+grid_b[1]+grid_c[1]+grid_d[1]
        
    ratio = (y_interval[1] - y_interval[0]) / (x_interval[1] - x_interval[0])
    if ratio > 1:
        plt.figure(figsize=(10, 10 * ratio))
    else:
        plt.figure(figsize=(10 / ratio, 10))
    x = np.linspace(x_interval[0], x_interval[1], delicacy)
    y = np.linspace(y_interval[0], y_interval[1], delicacy)
    X, Y = make_grid(x, y)

    # Draw axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Draw arrows on the axes
    plt.annotate('', xy=(x_interval[1], 0), xytext=(x_interval[0], 0),
                 arrowprops=dict(arrowstyle="->", color='black'))
    plt.annotate('', xy=(0, y_interval[1]), xytext=(0, y_interval[0]),
                 arrowprops=dict(arrowstyle="->", color='black'))

    for function, contour, color, label in zip(functions, contours, colors, labels):
        Z = function(X, Y)
        plt.contour(X, Y, Z, levels=[contour], colors=color)
        plt.plot([], [], color=color, label=label)
    
    circle = plt.Circle((1, 0), 0.03, color="blue", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(1.15, 0.05, '$A$', horizontalalignment='center', fontsize=font_size)  # Adjust position and label as needed

    circle = plt.Circle((math.cos(2), math.sin(2)), 0.03, color="blue", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(math.cos(2) + 0.05, math.sin(2) + 0.1, '$P$', horizontalalignment='center', fontsize=font_size)  # Adjust position and label as needed


    plt.text(0.2, 0.2, '$\\theta$', horizontalalignment='center', fontsize=font_size)  # Adjust position and label as needed

    plt.xlabel('$x$', fontsize=font_size)
    plt.ylabel('$y$', fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.title(title, fontsize=font_size)
    plt.grid(True)
    # plt.legend(fontsize=font_size)
    plt.savefig(f"{graph_name}.png", transparent=True)


plot_implicit_functions([circ, sml_circ, rad1, rad2], "", [1, 0.04, 0, 0], ["", "", "", ""], (-1.25, 1.25), (-1.25, 1.25), "unit_circle_1", 16)
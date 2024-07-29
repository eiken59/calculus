import numpy as np
import matplotlib.pyplot as plt

color_pool = ["blue", "olive", "violet", "navy", "lime", "slategrey", "hotpink"]

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
    for function, contour, color, label in zip(functions, contours, colors, labels):
        Z = function(X, Y)
        plt.contour(X, Y, Z, levels=[contour], colors=color)
        plt.plot([], [], color=color, label=label)
    plt.xlabel('$x$', fontsize=font_size)
    plt.ylabel('$y$', fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.title(title, fontsize=font_size)
    plt.grid(True)
    plt.legend(fontsize=font_size)
    plt.savefig(f"{graph_name}.png", transparent=True)

def plot_vectors(vectors, labels, title, graph_name, font_size):
    colors = color_pool[:len(vectors)]
    plt.figure(figsize=(10, 10))
    np_vectors = np.array(vectors)
    origin = np.zeros((2, len(vectors)))
    # Create an empty list to store legend handles
    legend_handles = []
    
    for vector, color, label in zip(np_vectors, colors, labels):
        # Plot each vector individually to get handles for the legend
        handle = plt.quiver(*origin[:, 0:1], vector[0:1], vector[1:2], color=color, scale=8)
        legend_handles.append(handle)

    # Add labels at the end of each vector for clarity
    for vector, color, label in zip(np_vectors, colors, labels):
        plt.text(vector[0]-0.5, vector[1]+0.25, label, color=color, fontsize=font_size, ha='left', va='bottom')

    # plt.quiver(*origin, np_vectors[:, 0], np_vectors[:, 1], color=colors, scale=8)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.title(title, fontsize=font_size)
    plt.grid(True)
    # plt.legend(fontsize=font_size)
    plt.xlim(right=4, left=-4)
    plt.ylim(bottom=-4, top=4)
    plt.savefig(f"{graph_name}.png", transparent=True)
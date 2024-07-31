import numpy as np
import matplotlib.pyplot as plt
import math

def fun1(x, y):
    return y - ((x-1) ** 3 - 2 * (x-1) ** 2 + 1)

def fun2(x, y):
    return y - 1 + 0.8 * (x-1)

def fun3(x, y):
    return y - 1 + 0.4 * (x-1)

def fun4(x, y):
    return y - 1 + 0.1 * (x-1)


color_pool = ["blue", "olive", "hotpink", "red", "red", "hotpink", "blacl", "hotpink"]

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
    # plt.axhline(0.4, color='black', linewidth=1)
    # plt.axvline(0.8, color='black', linewidth=1)

    # Draw arrows on the axes
    plt.annotate('', xy=(x_interval[1], 0), xytext=(x_interval[0], 0),
                 arrowprops=dict(arrowstyle="->", color='black'))
    plt.annotate('', xy=(0, y_interval[1]), xytext=(0, y_interval[0]),
                 arrowprops=dict(arrowstyle="->", color='black'))

    for function, contour, color, label in zip(functions, contours, colors, labels):
        Z = function(X, Y)
        plt.contour(X, Y, Z, levels=[contour], colors=color)
        plt.plot([], [], color=color, label=label)

    circle = plt.Circle((1, 1), 0.008, color="blue", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(1.02, 1.02, '$A$', horizontalalignment='center', fontsize=font_size, color='blue')  # Adjust position and label as needed

    circle = plt.Circle((1.0513, 0.9949), 0.008, color="red", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(1.065, 1.01, '$P_3$', horizontalalignment='center', fontsize=font_size, color='red')  # Adjust position and label as needed
    
    circle = plt.Circle((1.225, 0.91), 0.008, color="hotpink", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(1.227, 0.93, '$P_2$', horizontalalignment='center', fontsize=font_size, color='hotpink')  # Adjust position and label as needed

    circle = plt.Circle((1.553, 0.558), 0.008, color="olive", fill=True)  # Adjust the radius and color as needed
    plt.gca().add_patch(circle)
    plt.text(1.558, 0.575, '$P_1$', horizontalalignment='center', fontsize=font_size, color='olive')  # Adjust position and label as needed

    plt.xlabel('$x$-axis', fontsize=font_size)
    plt.ylabel('$y$-axis', fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.title(title, fontsize=font_size)
    plt.grid(True)
    # plt.legend(fontsize=font_size)
    plt.savefig(f"{graph_name}.png", transparent=True)


plot_implicit_functions([fun1, fun2, fun3, fun4], "", [0, 0, 0, 0], ["", "", "", ""], (0.75, 1.75), (0.25, 1.25), "sec_to_tan", 28)
import plot_tool

def inv(x, y):
    return y - 1 / x

def vert(x, y):
    return x

plot_tool.plot_implicit_functions([inv, vert], "The graph of $f(x)=\dfrac{1}{x}$", [0, 0], ["$f(x)=\dfrac{1}{x}$", "x=0"], (-6, 6), (-6, 6), "reciprocal_of_x", 14, 10000)
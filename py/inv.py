import plot_tool
import numpy as np

def inv(x, y):
    return np.where(np.abs(x) > 0.1, y - 1 / x, np.nan)

plot_tool.plot_implicit_functions([inv], "", [0], ["$f(x)=\dfrac{1}{x}$"], (-6, 6), (-6, 6), "limit_of_reci", 16, 10000)
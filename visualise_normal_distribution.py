"This program shows that histogram is better at showing normal distribution"
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    np.random.seed(100)

    # create a positively correlated array
    size = 500
    y = np.random.normal(0, 10, size)
    x = np.array(range(size))

    if len(sys.argv) > 1 and sys.argv[1] == "scatter":
        plt.scatter(x, y)
    else:
        plt.hist(x=y, bins='auto', color='#0504aa',
                 alpha=0.7, rwidth=0.85)

    plt.show()

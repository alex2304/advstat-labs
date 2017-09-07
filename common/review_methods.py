import scipy
from pandas.core.groupby import DataFrameGroupBy
from scipy.stats import norm, ttest_ind, ttest_rel

import numpy as np
from numpy import random
import plotly
import matplotlib.pyplot as plt

import pandas as pd
from statsmodels.stats.multitest import multipletests
from sympy.stats import cdf

if __name__ == '__main__':
    # np.cov(ddof=0)
    # x = np.arange(50, step=10)
    # ttest_ind
    # norm.sf()
    # plt.hist()
    # np.array().std
    # DataFrameGroupBy()
    # multipletests
    x = random.random(100)

    r = random.uniform(0, 5, 100)

    plt.boxplot(x)

    orig = np.random.uniform(0, 10, 1200)
    h = plt.hist(orig, bins=120, normed=True)

    orig = h[0]
    t = h[1]

    ax = plt.subplot(2, 3, 1)
    ax.set_title("f")
    ax.plot(t[:-1], orig)

    plt.figure(figsize=(20, 10))

    print(r)

    plt.show()



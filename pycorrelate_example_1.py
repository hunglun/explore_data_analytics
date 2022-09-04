import numpy as np
import pycorrelate as pyc

np.random.seed(1)
size = 10**3


def test_correlate_no_time_lag():
    t = np.sort(np.random.randint(0, 10**5, size=size))
    u = t
    lags = np.arange(0, 20)
    G = pyc.pcorrelate(t, u, lags)
    assert(max(G) == G[0])  # no time lag!


def test_correlate_1_time_lag():
    t = np.sort(np.random.randint(0, 10**5, size=size))
    u = t + [1] * t.size
    lags = np.arange(0, 20)
    G = pyc.pcorrelate(t, u, lags)
    assert(max(G) == G[1])  # 1 time unit lag!

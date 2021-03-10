import pytest
from os import path
import numpy as np


@pytest.fixture
def flac_filename(tmp_path):
    return path.join(tmp_path, "test.flac")
    # return "test/test.flac"


@pytest.fixture
def fs():
    return 8000


@pytest.fixture
def xmax():
    return lambda dtype: 2 ** (8 * np.dtype(dtype).itemsize - 1) - 1


@pytest.fixture
def samples(xmax):
    T = 1

    def fun(dtype, fs, ch, A=None):
        N = int(fs * T)
        t = np.arange(N).reshape((N, 1)) / fs
        f0 = np.tile(np.array(((1001,),)), (1, ch))
        C = np.cos(2 * np.pi * (f0 * t + np.random.rand(1, ch)))
        if ch == 1:
            C = C.ravel()
        if A is None:
            A = xmax(dtype)

        x = (A * C).astype(dtype)

        if dtype == np.int32:
            x = np.left_shift(np.right_shift(x, 8), 8)

        return x

    return fun

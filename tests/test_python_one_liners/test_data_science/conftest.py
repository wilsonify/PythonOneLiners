"""
conftest for data_science module
"""
import numpy as np
import pytest


@pytest.fixture(name="basket")
def basket_fixture():
    """ test fixture for market basket analysis """
    return np.array(
        [
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
        ]
    )

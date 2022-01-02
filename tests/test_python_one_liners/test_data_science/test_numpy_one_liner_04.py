from python_one_liners.data_science.numpy_one_liner_04 import find_superstars


def test_smoke():
    print("fire?")


def test_find_superstars():
    # Boolean Indexing to Filter Two-Dimensional Arrays

    # Dependencies
    import numpy as np

    # Data: popular Instagram accounts (millions followers)
    inst = np.array(
        [
            [232, "@instagram"],
            [133, "@selenagomez"],
            [59, "@victoriassecret"],
            [120, "@cristiano"],
            [111, "@beyonce"],
            [76, "@nike"],
        ]
    )

    # One-liner
    superstars = find_superstars(inst)

    # Results
    assert superstars.tolist() == [
        "@instagram",
        "@selenagomez",
        "@cristiano",
        "@beyonce",
    ]

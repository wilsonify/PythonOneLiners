from python_one_liners.data_science.numpy_one_liner_02 import selective_increase


def test_smoke():
    print("fire?")


def test_selective_increase():
    # Working with NumPy Arrays: Slicing, Broadcasting, and Array Types

    # Dependencies
    import numpy as np

    # Data: yearly salary in ($1000) [2025, 2026, 2027]
    data_scientist = [130, 132, 137]
    product_manager = [127, 140, 145]
    designer = [118, 118, 127]
    software_engineer = [129, 131, 137]
    employees = np.array([data_scientist, product_manager, designer, software_engineer])

    # One-liner
    selective_increase(employees)

    # Result

    assert employees.tolist() == [
        [143, 132, 150],
        [127, 140, 145],
        [118, 118, 127],
        [129, 131, 137],
    ]

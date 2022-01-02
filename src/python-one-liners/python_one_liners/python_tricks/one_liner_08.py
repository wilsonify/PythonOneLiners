""" Analyzing Cardiac Health Data with List Concatenation """


def clean_cycle(cardiac_cycle):
    """
    clean the original list by removing the redundant first and the last two data values
    [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62] becomes [60, 62, 64, 68, 77, 80, 76, 71, 66, 61].
    concatenate the same list again and again to create a larger list
    """

    return cardiac_cycle[1:-2] * 10


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Data
    cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

    # One-Liner
    expected_cycles = clean_cycle(cardiac_cycle)

    # Result
    plt.plot(expected_cycles)
    plt.show()

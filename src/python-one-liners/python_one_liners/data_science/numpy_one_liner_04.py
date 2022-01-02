# Boolean Indexing to Filter Two-Dimensional Arrays
def find_superstars(inst):
    """
    pull the names of the Instagram influencers with more than 100 million followers
    :return:
    """
    return inst[inst[:, 0].astype(float) > 100, 1]


if __name__ == "__main__":
    # Dependencies
    import numpy as np

    # Data: popular Instagram accounts (millions followers)
    inst_outer = np.array(
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
    superstars = find_superstars(inst_outer)

    # Results
    print(superstars)
    """
    ['@instagram' '@selenagomez' '@cristiano' '@beyonce']
    """

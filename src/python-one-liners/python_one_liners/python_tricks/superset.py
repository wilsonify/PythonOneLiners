from functools import reduce

if __name__ == "__main__":
    # Superset Python One-Liner
    lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
def swaparoo(a, b):
    return b, a


if __name__ == "__main__":
    # Swap Two Variables Python One-Liner
    a = 10
    b = 100000
    print(f"a={a}")
    print(f"b={b}")
    a, b = swaparoo(a, b)
    print(f"a={a}")
    print(f"b={b}")

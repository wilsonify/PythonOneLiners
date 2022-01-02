def qsort(L):
    """ Quicksort Python One-liner """
    return [] if L == [] else qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + qsort([x for x in L[1:] if x >= L[0]])


if __name__ == "__main__":
    print(qsort([100, 12321, 34, 67, 2, 46]))  # [2, 34, 46, 67, 100, 12321]

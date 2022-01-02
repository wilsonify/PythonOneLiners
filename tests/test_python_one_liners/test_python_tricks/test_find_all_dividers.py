def test_smoke():
    print("fire?")


def find_dividers(your_number):
    """ Find all dividers of a number """
    return [divider for divider in range(1, your_number) if your_number % divider == 0]


def test_q():
    assert find_dividers(100) == [1, 2, 4, 5, 10, 20, 25, 50]

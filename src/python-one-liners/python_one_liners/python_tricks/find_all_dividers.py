def find_dividers(your_number):
    """ Find all dividers of a number """
    return [divider for divider in range(1, your_number) if your_number % divider == 0]


if __name__ == "__main__":
    print(find_dividers(100))  # [1, 2, 4, 5, 10, 20, 25, 50]

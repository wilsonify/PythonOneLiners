def spi(input_str):
    """ space separated integers into a list"""
    return list(map(int, input_str.split()))


if __name__ == "__main__":

    print(spi(input()))

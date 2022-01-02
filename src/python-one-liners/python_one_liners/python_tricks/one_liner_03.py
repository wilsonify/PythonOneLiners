def readafile(path_to_file):
    """ Reading a File """
    return [line.strip() for line in open(path_to_file)]


if __name__ == "__main__":
    print(readafile("one_liner_3.py"))  # Output: <This file content>

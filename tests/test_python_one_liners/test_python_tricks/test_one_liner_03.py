import os.path

from python_one_liners.python_tricks.one_liner_03 import readafile


def test_smoke():
    print("fire?")


def test_readafile():
    path_to_this_file = os.path.abspath(__file__)
    assert readafile(f"{path_to_this_file}")[:10] == [
        'import os.path',
        '',
        'from python_one_liners.python_tricks.one_liner_03 import readafile',
        '',
        '',
        'def test_smoke():',
        'print("fire?")',
        '',
        '',
        'def test_readafile():'
    ]

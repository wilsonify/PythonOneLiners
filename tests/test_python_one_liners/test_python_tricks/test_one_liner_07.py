from python_one_liners.algorithms.algorithms_one_liner_10 import q


def test_smoke():
    print("fire?")


def test_q():


    # Using Slice Assignment to Correct Corrupted Lists


    # Data
    visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
                'Safari', 'corrupted', 'Safari', 'corrupted',
                'Chrome', 'corrupted', 'Firefox', 'corrupted']

    # One-Liner
    visitors[1::2] = visitors[::2]

    # Result
    print(visitors)
    '''
    ['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari',
    'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox']
    '''

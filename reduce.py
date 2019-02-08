"""
Sum all the elements in an array by splitting it in half recursively
"""


def reduce(arr, step=0):
    """
    :param arr: the input array
    :param step: the recursion step

    :return: 2-tuple (sum of elements, steps required)
    """
    q, r = divmod(len(arr), 2)

    if q == 0:
        # single element in the array, we're done
        if r == 0:
            # empty array returns unknown value
            return None, None
        return arr[0], step

    # prepend zero to first part for odd length array
    first = arr[:q] if r == 0 else [0] + arr[:q]
    second = arr[q:]

    result = [sum(x) for x in zip(first, second)]
    return reduce(result, step + 1)


if __name__ == '__main__':
    test_array = [33, 6, 9, 1, 23, 88, 2]
    result, step = reduce(test_array)
    print(result, step)

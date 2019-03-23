"""
given a [int], only contains no-negative numbers, catancate them as a whole, return largest number
Given two numbers X and Y, how should myCompare() decide which number to put first –
we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y)
"""
from functools import cmp_to_key


@cmp_to_key
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    # return ((int(ba) > int(ab)) - (int(ba) < int(ab)))  True - False
    if ab == ba:
        return 0
    elif ab > ba:
        return -1
    else:
        return 1


if __name__ == "__main__":
    a = [54, 546, 548, 60]
    sorted_array = sorted(a, key=comparator)
    number = "".join([str(i) for i in sorted_array])
    print(number)

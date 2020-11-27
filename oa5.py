"""
给一个数组有n个元素，可以进行把最左边的数字挪到最右边的操作。判断数组经过一定次数操作是否能变成[1, 2 …n] 或者 [n…1]
例子1.  [3,4,5,1,2] 一定操作后可变成1，2，3，4，5， 返回True
例子2. [2,3,1,4] return false
"""
from typing import List


def is_permutation(A, n):
    table = [False] * n
    for a in A:
        if a <= 0:
            return False
        if table[a - 1]:
            return False
        table[a - 1] = True
    return all(table)


def has_n_to_1(B: List[int], n: int):
    idx = B.index(1)
    for i in range(idx + 1, idx + n):
        if B[i] != i - idx + 1:
            return False
    return True


def has_1_to_n(B: List[int], n: int):
    idx = B.index(n)
    for i in range(idx + 1, idx + n):
        if B[i] != n - (i - idx):
            return False
    return True


def solve(A: List[int]) -> bool:
    n = len(A)
    if not is_permutation(A, n):
        return False
    B = A * 2
    return any([has_1_to_n(B, n), has_n_to_1(B, n)])


if __name__ == '__main__':
    A1 = [3, 4, 5, 1, 2]
    assert solve(A1)

    A2 = [2, 3, 1, 4]
    assert not solve(A2)

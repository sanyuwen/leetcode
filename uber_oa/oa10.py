"""
在数组里找i < j, a[j] + a[j] 是2的power。有多少个i, j pair。数组长度<10^6, 每个数的大小[-10^5, 10^5]
"""
from typing import List


def is_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)


def solve(A: List[int]):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            target = A[i]+A[j]
            if is_power_of_two(target):
                print("{} + {} = {}".format(A[i], A[j], target))


if __name__ == '__main__':
    solve([2, 6, 14, 1, 4, 30])

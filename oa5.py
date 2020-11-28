"""
给一个数组有n个元素，可以进行把最左边的数字挪到最右边的操作。判断数组经过一定次数操作是否能变成[1, 2 …n] 或者 [n…1]
例子1.  [3,4,5,1,2] 一定操作后可变成1，2，3，4，5， 返回True
例子2. [2,3,1,4] return false
"""
from typing import List


def solve(A: List[int]) -> bool:
    n = len(A)
    B = "".join(str(t) for t in A * 2)
    n_to_1 = "".join(str(t) for t in range(n, 0, -1))
    one_to_n = "".join(str(t) for t in range(1, n+1))
    return n_to_1 in B or one_to_n in B


if __name__ == '__main__':
    A1 = [3, 4, 5, 1, 2]
    assert solve(A1)

    A2 = [2, 3, 1, 4]
    assert not solve(A2)

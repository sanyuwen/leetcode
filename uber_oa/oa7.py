"""
输入正整数数组A，返回01数组B，B[i]表示A[i] A[i+1] A[i+2]能否组成三角形。
"""
from typing import List


# a<=b<=c, if a+b>c, can form a triangle
def can(B: List[int]) -> bool:
    C = sorted(B)
    return C[0] + C[1] > C[2]


def solve(A: List[int]) -> List[int]:
    n, ans = len(A), []
    for i in range(n - 2):
        if can([A[i], A[i + 1], A[i + 2]]):
            ans.append(1)
        else:
            ans.append(0)
    return ans


if __name__ == '__main__':
    assert solve([1, 2, 3, 4, 6, 8, 20]) == [0, 1, 1, 1, 0]

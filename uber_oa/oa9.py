"""
 给一个数组，返回子数组个数，子数组满足：所有元素都出现至少2次。
  比如[1,2,1,2,4]返回1（[1,2,1,2]），[1,2,3,3,3,2,4]返回4（[3,3], [3,3], [3,3,3], [2,3,3,3,2]）
"""
from typing import List
from collections import defaultdict, Counter


def solve(A: List[int]) -> int:
    n = len(A)
    # 2 pointers
    ans = 0
    for i in range(n - 1):
        for j in range(i, n):
            if all(v >= 2 for v in Counter(A[i:j + 1]).values()):
                ans += 1
    return ans


if __name__ == '__main__':
    assert solve([1, 2, 1, 2, 4]) == 1
    print()
    assert solve([1, 2, 3, 3, 3, 2, 4]) == 4

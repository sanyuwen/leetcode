"""
给一个数组，连续3个字母不相同计数加一，找出array里有多少, 1,2,3,4 -> 2    1,2,3,3 -> 1
"""
from typing import List
from collections import OrderedDict


def solve(A: List[int]) -> int:
    window, ans = OrderedDict(), 0
    for i, a in enumerate(A):
        if a not in window and len(window) == 2:
            ans += 1
            window.popitem(last=False)
        window[a] = i
    return ans


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 3], 1)
    ]
    for input, output in cases:
        assert output == solve(input)
        print(output)

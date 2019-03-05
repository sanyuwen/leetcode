from collections import defaultdict
from itertools import product
import unittest


def fourSum(nums, target):
    mmap = defaultdict(list)
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            mmap[nums[i]+nums[j]].append((i,j))
    resuls = set()
    for k in mmap:
        k_ = target-k
        if k_ in mmap:
            list1, list2 = mmap[k], mmap[k_]
            for (a,b), (c,d) in product(list1, list2):
                if not any((a==c, a==d, b==c, b==d)):
                    resuls.add(tuple(sorted([nums[a],nums[b],nums[c],nums[d]])))
    return [list(item) for item in resuls]


class TestSolution(unittest.TestCase):

    def test_solution(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        ans = [
            [-1, 0, 0, 1],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2]
        ]
        self.assertListEqual(fourSum(nums, target), ans)


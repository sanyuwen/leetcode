from collections import defaultdict
from bisect import bisect

def fourSum(nums, target):
    mmap = defaultdict()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            mmap[nums[i]+nums[j]].append((i,j))
    resuls = set()
    for k in mmap:
        k_ = target-k
        if k_ in mmap:
            list1, list2 = mmap[k], mmap[k_]






class TestSolution(unittest.TestCase):

    def test_solution(self):
        pass


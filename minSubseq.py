import unittest

from collections import defaultdict
from bisect import bisect


def min_subsequences(source, target):
    # assume target != ""
    # assume all characters of target is in source
    if len(target) == 1:
        return 1
    else:
        mmap = defaultdict(list)
        for i,k in enumerate(source):
            mmap[k].append(i)

        ans, pre = 1, mmap[target[0]][0]
        for t in target[1:]:
            ilist = mmap[t]
            index = bisect(ilist, pre)
            if index == len(ilist):
                ans += 1
                pre = ilist[0]
            else:
                pre = ilist[index]
        return ans


class TestSolution(unittest.TestCase):

    def test_solution(self):
        cases = []
        cases.append(("abc", "abcab"))
        cases.append(("abc", "bacbaac"))
        cases.append(("abc", "b"))
        cases.append(("abcab", "bacbaac"))
        cases.append(("abcab", "abcab"))
        cases.append(("abcab", "bbaacabc"))
        cases.append(("abcab", "bacba"))
        cases.append(("abc", "abcab"))
        cases.append(("abac", "abcab"))
        cases.append(("abacbab", "abcab"))
        cases.append(("abacbab", "abcabb"))
        cases.append(("bacbab", "abcabb"))

        ans = []
        ans.append(2)
        ans.append(5)
        ans.append(1)
        ans.append(4)
        ans.append(1)
        ans.append(4)
        ans.append(3)
        ans.append(2)
        ans.append(2)
        ans.append(1)
        ans.append(2)
        ans.append(3)

        self.assertEqual([min_subsequences(*case) for case in cases], ans)





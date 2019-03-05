import unittest
import re


def myAtoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    m = re.search(r"^[+-]?\d+", s.lstrip())
    try:
        n = int(m.group(0))
        if n>INT_MAX:
            return INT_MAX
        elif n<INT_MIN:
            return INT_MIN
        else:
            return n
    except AttributeError:
        return 0


class TestSolution(unittest.TestCase):

    def test_solution(self):
        cases = []
        cases.append("42")
        cases.append("   -42")
        cases.append("4193 with words")
        cases.append("words and 987")
        cases.append("-91283472332")

        ans = []
        ans.append(42)
        ans.append(-42)
        ans.append(4193)
        ans.append(0)
        ans.append(-2147483648)
        self.assertEqual([myAtoi(n) for n in cases], ans)

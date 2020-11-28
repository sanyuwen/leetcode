"""
给两个input: List<string> s1, s2, 问list中的每个string在s2的substring中最多出现几次。 
比如s1 ="ab", s2="ababcbabc", s1在substring "abab"里出现两次，就要返回2。另一个例子比如s1 = "abab", s2="abababab",也需要返回2.
"""
from typing import List


def all_indexs(s1: str, s2: str) -> List[int]:
    # return all indexs in s1 for s2
    m, n, i, ans = len(s1), len(s2), 0, []
    while i < m:
        try:
            index = s1.index(s2, i)
            ans.append(index)
            i = index + n
        except Exception:
            break
    return ans


def solve(s1: str, s2: str) -> int:
    ids = all_indexs(s1, s2)
    print(ids)
    n, ans = len(s2), 0
    if len(ids) <= 1:
        return len(ids)
    cur = 1
    for a, b in zip(ids, ids[1:]):
        if b == a + n:
            cur += 1
        else:
            ans = max(ans, cur)
            cur = 1
    ans = max(ans, cur)
    return ans


if __name__ == '__main__':
    assert solve("ababcbabc", "ab") == 2
    assert solve("abababab", "abab") == 2
    assert solve("ababcabab", "abab") == 1
    assert solve("abababcab", "ab") == 3

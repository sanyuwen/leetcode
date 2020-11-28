"""
一个字符串，删除从index 0开始开头的最长的palindrome，删除到没办法删除为止（palindrome长度是1的话不算），返回结果
"""


def solve(s: str) -> str:
    # dp[i][j], 0<=i<=j<len(s), true if s[i..j] is palindrome
    # insight from https://leetcode.com/problems/longest-palindromic-substring/
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i] = True
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    dp[n - 1][n - 1] = True
    for t in range(2, n):
        for i in range(n - t):
            if s[i] == s[i + t] and dp[i + 1][i + t - 1]:
                dp[i][i + t] = True
    # utilize information above, we solve this problem
    # for r in dp:
    #     print(r)
    idx = 0
    while idx < n - 1:
        i = n - 1
        while i > idx and not dp[idx][i]:
            i -= 1
        if i == idx:
            # no palindrome any more
            break
        idx = i + 1
    return s[idx:]


if __name__ == '__main__':
    s = "babddc"
    assert solve(s) == "c"

    s = "babbabdc"
    assert solve(s) == "dc"

    s = "bbaabbdaccadca"
    assert solve(s) == "ca"

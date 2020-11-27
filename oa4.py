"""
一个字符串，删除从index 0开始开头的最长的palindrome，删除到没办法删除为止（palindrome长度是1的话不算），返回结果
"""


def solve(s: str) -> str:
    # dp[i][j], 0<=i<=j<len(s), true if s[i..j] is palindrome
    n = len(s)
    dp = [[True] * n for _ in range(n)]
    ans = (0, 1)
    for i in range(n - 1):
        dp[i][i + 1] = True if s[i] == s[i + 1] else False
        if dp[i][i + 1]:
            ans = (i, i + 2)
    for t in range(2, n):
        for i in range(n - t):
            dp[i][i + t] = True if s[i] == s[i + t] and dp[i + 1][i + t - 1] else False
            if dp[i][i + t]:
                ans = (i, i + t + 1)


if __name__ == '__main__':
    s = "babddc"
    assert solve(s) == "c"

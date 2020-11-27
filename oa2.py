"""
两个人a和b玩消消乐，给一个数组，如果里面有两个连续一样的数就消除掉，轮下一个人，问最后谁赢，返回名字字符串
"""
from typing import List


# using stack, return how many times the delete operation can be done
def solve(A: List[int]) -> int:
    stack, ans = [], 0
    for a in A:
        if stack and stack[-1] == a:
            stack.pop()
            ans += 1
    return ans


if __name__ == '__main__':
    A = [3, 4, 5, 5, 4, 6]
    assert solve(A) % 2 == 0

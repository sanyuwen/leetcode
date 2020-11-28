"""

给一个矩阵 。代表空白 #代表箱子 *代表障碍 问把矩阵顺时针旋转90度后箱子下落后的样子

输入：
###。。
#。*##
##。*#

输出
。。。
##。
#*#
*##
###

"""
from typing import List


def transform_segment(A: List[str], lo: int, hi: int):
    while lo < hi:
        while lo < hi and A[lo] == '。':
            lo += 1
        while lo < hi and A[hi] == '#':
            hi -= 1
        A[lo], A[hi] = A[hi], A[lo]
        lo += 1
        hi -= 1


def transform_row(A: List[str]) -> List[str]:
    lo, hi = -1, 0
    for a in A:
        if a == '*':
            transform_segment(A, lo + 1, hi - 1)
            lo = hi
        hi += 1
    transform_segment(A, lo + 1, hi - 1)
    return A


def solve(A: List[str], r: int, c: int) -> List[str]:
    C = [transform_row(list(row)) for row in A]
    ans = []
    for i in range(c):
        ans.append("".join([C[j][i] for j in range(r-1, -1, -1)]))
    return ans


if __name__ == '__main__':
    A = ["###。。", "#。*##", "##。*#"]
    B = solve(A, 3, 5)
    for b in B:
        print(b)

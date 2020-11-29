"""
1. 给一个int，然后从最大位两两reverse，位数为奇数的话，最后一位保持不变。
64839 - 》 46389


2. 给一个手机键盘的图片，每个数字上对应一些字母。给一个数组，是可以使用的按键数字，在一个组String，判断这些String都能不能用给的按键数字打出来。

3. 这个题目出现了好多好多次

1）其中一个人这样描述题目：

自动股票交易机器人，给一个长度为n的0，1数组 代表 机器人第 i 天的决策：0 是 买， 1 是卖。再给一个同样长度的矩阵代表 第 i 天的股价。你有一个机会将连续 k 的操作全变成卖，求最大revenue。Assumption 是你一开始就有足够多的股票，不用担心先买还是先卖，只需要求这n天内最大revenue操作。
这题我觉得和平时的股票题无关。买就是减，卖就是加，其实就是划窗求最大值，类似 梨扣夷芊凌邬💩尔

2 ） 另一个这样描述题目：
最大化股市收益，要求输出一个整数
输入是两个数组和一个int k
第一个为prices，是股市每天的价格
第二个为algo，里面为0 或者1， 分别代表买和卖。
然后k代表连续卖的天数。


举例：
prices 为 -2, 5, 7, -3
algo   为 0, 0, 0, 0
k         为 2


那么原本的algo操作为 0,0,0,0 可以变化为如下可能
1,1,0, 0
0,1,1,0
0,0, 1,1


计算这几种状况下的收益，取最大值输出即可


附另一个例子：
prices -2， 4， -1， -5， 2 ，-6， -7
algo     0,   1,     0,     1,     1,     0,     1
k = 1

上面两个描述我认为是一道题目

4
给一个二维矩阵，每一行的第一列的数字，称之为pivot，要求对这些pivot进行排序。
排序的comparator不是基于这些pivot的值，而是他们的 “右上-右下-对角线sum”，这个对角线sum的定义是，从这个pivot 开始向右上方挪动，到顶之后再像右下方挪动，这样遍历下来的sum称之为对角线sum。
"""


def solve_1(num: int):
    A = list(str(num))
    n = len(A)
    for i in range(0, n, 2):
        if i + 1 < n:
            A[i], A[i + 1] = A[i + 1], A[i]
    return int("".join(A))


def solve_3(prices, algo, k):
    n, ans = len(prices), ans
    for i in range(n - k + 1):
        cur = algo[:]
        for j in range(i, i + k):
            cur[j] = 1
        revenue = 0
        for a, b in zip(prices, cur):
            revenue += a if b == 1 else -a
        ans = max(revenue, ans)
    return ans


if __name__ == '__main__':
    assert solve_1(64839) == 46389

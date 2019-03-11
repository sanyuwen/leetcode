"""
given a set, return power set of it.
"""


def power_set1(n, indexarr, cur, a_list, ans):
    # from left to right selection
    ans.append([a_list[t] for t in indexarr[:cur]])
    s = 0 if cur == 0 else indexarr[cur - 1] + 1
    for i in range(s, n):
        indexarr[cur] = i
        power_set1(n, indexarr, cur + 1, a_list, ans)


def power_set2(n, decision_arr, cur, a_list, ans):
    # decision binary tree of select this element or not
    if cur < n:
        decision_arr[cur] = 1  # select this element
        power_set2(n, decision_arr, cur + 1, a_list, ans)
        decision_arr[cur] = 0
        power_set2(n, decision_arr, cur + 1, a_list, ans)
    else:
        ans.append([t for t, b in zip(a_list, decision_arr) if b == 1])


def power_set3(n, a_list, ans):
    # 0 to 2**n-1 binary repretation conrrensponding to a subset
    for num in range(2 ** n):
        binary = bin(num)[2:].rjust(n, '0')
        ans.append([t for t, b in zip(a_list, binary) if b == '1'])


if __name__ == '__main__':
    a = [t for t in "abcde"]
    n = len(a)
    indexarr = [0] * n
    ans1 = []
    power_set1(n, indexarr, 0, a, ans1)
    # print("total of subsets is {}".format(len(ans)))
    # for item in ans:
    #     print(item)
    ans2 = []
    power_set2(n, indexarr, 0, a, ans2)
    for item in ans2:
        if not item in ans1:
            print("not match for ans2")
            break

    ans3 = []
    power_set3(n, a, ans3)
    for item in ans3:
        if not item in ans1:
            print("not match for ans3")
            break

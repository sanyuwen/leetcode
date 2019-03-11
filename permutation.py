from itertools import permutations


def get_permutation(n, indexarr, cur, a_list, ans):
    if cur < n:
        for i in range(1, n + 1):
            if not i in indexarr[:cur]:
                indexarr[cur] = i
                get_permutation(n, indexarr, cur + 1, a_list, ans)
    else:
        ans.append([a_list[t - 1] for t in indexarr])


def permutation(a_list):
    n = len(a_list)
    indexarr = [0] * n
    ans = []
    get_permutation(n, indexarr, 0, a_list, ans)
    return ans


if __name__ == '__main__':
    a = [t for t in "abcde"]
    ans = permutation(a)
    print(ans)

    bench = [list(t) for t in permutations(a)]
    for item in ans:
        if not item in bench:
            print("not match")
            break

    assert ans == bench

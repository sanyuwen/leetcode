"""
 give you a n * n matrix， divide into size * size block

 for example (input)  :
 1 2 | 3 4
 5 6 | 7 8
 -----------
 3 2 | 1 4
 1 5 | 2 3

your  job

 1)
find the first missing positive number and then sort

 3 | 1        sort                   1 | 3
 ------     --------
 4 | 5                               4 | 5


 2 )
 and then rearrange the original matrix based on the sored missing positive number

 output:
 3 4 | 1 2
 7 8 | 5 6
 -----------
 3 2 | 1 4
 1 5 | 2 3
"""
from typing import List


def get_index(i: int, j: int, size: int, r: int) -> int:
    return i // size * r + j // size


def divide(n: int, size: int, B: List[List[int]]) -> List[List[int]]:
    r = n // size
    ans = [[] for _ in range(r * r)]
    for i in range(n):
        for j in range(n):
            index = get_index(i, j, size, r)
            ans[index].append(B[i][j])
    return ans


def combine(n: int, size: int, B: List[List[int]]) -> List[List[int]]:
    ans = [[0] * n for _ in range(n)]
    r = n // size
    for i in range(n):
        for j in range(n):
            index = get_index(i, j, size, r)
            ans[i][j] = B[index].pop(0)
    return ans


def first_missing_positive_number(row: List[int]) -> int:
    x = len(row)
    for i in range(1, x + 1):
        if i not in row:
            return i
    return x + 1


# guarantee n%size==0
def solve(n: int, size: int, B: List[List[int]]) -> List[List[int]]:
    A = divide(n, size, B)
    print(A)
    A.sort(key=first_missing_positive_number)
    print(A)
    return combine(n, size, A)


if __name__ == '__main__':
    B = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [3, 2, 1, 4],
        [1, 5, 2, 5]
    ]
    ans = solve(4, 2, B)
    for row in ans:
        print(row)

"""
给你二维数组长和宽，起点坐标，终点坐标。一开始从起点按照(+1, +1)的方式走，x坐标出界就取相反数，y出界同理，走到角落就同时取反。问走到终点的步数，如果走不到返回-1.
"""
from typing import Tuple, List


def solve(r: int, c: int, s: Tuple[int, int], e: Tuple[int, int]) -> int:
    # keep track of all visited positions and directions, if it return to same positions and direction when not arrive
    # destination, it fails
    visited, dire = set(), (1, 1)
    a, b = s
    if a == r - 1 or a == 0:
        dire = (-dire[0], dire[1])
    if b == c - 1 or b == 0:
        dire = (dire[0], -dire[1])
    # adding current position along with legitimate direction
    visited.add((s, dire))
    cur = s

    def move(curp: Tuple[int, int], dire_: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        a_, b_ = curp
        a_ += dire_[0]
        b_ += dire_[1]
        if a_ == r - 1 or a_ == 0:
            dire_ = (-dire_[0], dire_[1])
        if b_ == c - 1 or b_ == 0:
            dire_ = (dire_[0], -dire_[1])
        return (a_, b_), dire_

    i=0
    while cur != e:
        cur, dire = move(cur, dire)
        nextc = (cur, dire)
        print(nextc)
        if nextc in visited:
            return False
        visited.add(nextc)
        i+=1
        if i==10:
            break
    return True


if __name__ == '__main__':
    assert solve(3, 4, (1, 0), (0, 1))
    assert not solve(3, 4, (1, 0), (0, 2))

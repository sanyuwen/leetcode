from collections import defaultdict, OrderedDict
import unittest


class LFUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = defaultdict(list)
        self.min = 0

    def get(self, key: int) -> int:
        try:
            value, times = super().__getitem__(key)
            self.move_to_end(key)
            newtimes = times + 1
            self.frequency[newtimes].append(key)
            self.frequency[times].remove(key)
            if len(self.frequency[times]) == 0:
                del self.frequency[times]
            super().__setitem__(key, (value, newtimes))
            return value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
            v, t = self[key]
            self[key] = (v, t + 1)
            self.frequency[t].remove(key)
            if len(self.frequency[t]) == 0:
                del self.frequency[t]
            self.frequency[t+1].append(key)
        else:
            if len(self) >= self.capacity:
                self.min = min(self.frequency)
                to_evicts = self.frequency[self.min]
                for k in self:
                    if k in to_evicts:
                        _, t = super().__getitem__(k)
                        self.frequency[t].remove(k)
                        if len(self.frequency[t]) == 0:
                            del self.frequency[t]
                        del self[k]
                        break
            super().__setitem__(key, (value, 0))
            self.frequency[0].append(key)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        commands = ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
        para = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
        t = LFUCache(2)
        for c, p in zip(commands, para):
            if c == "put":
                t.put(p[0], p[1])
                print(t)
                print(t.frequency)
                print()
            elif c=="get":
                v = t.get(p[0])
                print(v)
                print(t)
                print(t.frequency)
                print()



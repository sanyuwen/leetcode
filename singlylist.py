"""
从一个环状单项链表里删除node，要求是隔一个删一个,例子
输入：1-》2-》3-》4-》5-》6-》1
输出: 1-》3-》5-》1
"""
import unittest


class node:
    def __init__(self, value):
        self.val = value
        self.next = None


def jump_delete(head):
    p, q = head, head.next
    while q!=head:
        p.next = q.next
        q = q.next
        if q==head:
            break
        p = q
        q = p.next
        #print(p.val, q.val)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        valist = [1,2,3,4,5,6,7]
        head = node(valist[0])
        pre = head
        for item in valist[1:]:
            current = node(item)
            pre.next = current
            pre = current
        pre.next = head

        jump_delete(head)
        i = 0
        iter = head
        while i<8:
            print(iter.val, iter.next.val)
            iter = iter.next
            i+=1




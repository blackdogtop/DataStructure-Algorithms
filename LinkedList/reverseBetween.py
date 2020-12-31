#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/

92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        递归 + 递归反转前N
        Complexity:
            time: O(n) - n为参数
            space: O(n) - n为参数
        :param m, n: 1 <= m <= n <= 链表长度
        """
        def reverser(head, n: int):
            """反转链表前n个"""
            nonlocal successor
            if n == 1:
                successor = head.next
                return head
            last = reverser(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last

        successor = None
        if m == 1:
            return reverser(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    def reverseBetweenIter(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        递归 + 迭代链表前N
        Complexity:
            time: O(n) - n为参数
            space: O(m) - m为参数
        """
        def reverseN(head, N):
            p, n = head, N
            while n > 1:
                p = p.next
                n -= 1
            pos1 = p.next
            pos2 = head
            p.next = None
            while pos2:
                pos3 = pos2.next
                pos2.next = pos1
                pos1 = pos2
                pos2 = pos3
            return pos1

        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    def reverseBetweenIter2(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        迭代
        Complexity:
            time: O(n) - n为参数
            space: O(1)
        """
        dummy = ListNode(-1)
        pre = dummy
        pre.next = head

        for _ in range(1, m):
            pre = pre.next

        head = pre.next
        for _ in range(m, n):
            nex = head.next
            head.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    # res = s.reverseBetween(node1, 2, 4)  # 递归 + 递归反转前N
    # res = s.reverseBetweenIter(node1, 2, 4)  # 递归 + 迭代链表前N
    res = s.reverseBetweenIter2(node1, 2, 4)  # 迭代
    while res:
        print(res.val, end=' ')
        res = res.next


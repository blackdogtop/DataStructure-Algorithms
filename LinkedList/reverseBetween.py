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


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    res = s.reverseBetween(node1, 2, 4)
    while res:
        print(res.val, end=' ')
        res = res.next


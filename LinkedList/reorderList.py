#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/reorder-list/

143. 重排链表
给定一个单链表L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        中断 + 逆序 + 拼接
        Complexity:
            time: O(N) - 线性
            space: O(1)
        """
        if not head or not head.next: return head

        slow, fast = head, head.next
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        h2 = slow.next
        slow.next = None

        dummy = ListNode(-1)
        dummy.next = h2
        pre, cur = dummy, h2
        while cur.next:
            nex = cur.next
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
        h2 = dummy.next

        while head and h2:
            n1, n2 = head.next, h2.next
            head.next = h2
            h2.next = n1
            head = n1
            h2 = n2

    def reorderListStack(self, head: ListNode) -> None:
        """
        栈存储
        Complexity:
            time: O(N) - 线性
            space: O(N)
        """
        if not head: return head

        stack = []
        h = head.next
        while h:
            stack.append(h)
            h = h.next

        begin, end = 0, len(stack) - 1
        while begin <= end:
            head.next = stack[end]
            head = head.next
            end -= 1
            head.next = stack[begin]
            head = head.next
            begin += 1
        head.next = None

    def reorderListRecursion(self, head: ListNode) -> None:
        """
        递归
        Complexity:
            time: O(N/2logN) ? - N为链表节点个数
            space: O(N/2) ?
        """
        if not head or not head.next or not head.next.next: return
        cur = head
        while cur.next.next:
            cur = cur.next  # 导数第二个节点

        cur.next.next = head.next
        head.next = cur.next
        cur.next = None
        self.reorderListRecursion(head.next.next)


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    # s.reorderList(node1)  # 中点+逆序+重排
    s.reorderListStack(node1)  # 栈存储
    # s.reorderListRecursion(node1)  # 递归
    while node1:
        print(node1.val, end=' ')
        node1 = node1.next

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
        Do not return anything, modify head in-place instead.
        Complexity:
            time: O(3/2N) - N为链表节点数
            space: O(1)
        """
        def getMid():
            """获取链表中点并将其从中点处切断"""
            nonlocal head
            low, fast = head, head.next
            while fast and fast.next:
                low = low.next
                fast = fast.next.next
            h2 = low.next  # 第二段头节点
            low.next = None
            return h2

        def reverse(head):
            """逆序链表"""
            ptr1 = None
            ptr2 = head
            while ptr2:
                ptr3 = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2
                ptr2 = ptr3
            return ptr1

        def reorder(ptr1, ptr2):
            """重排链表"""
            while ptr1 and ptr2:
                n1 = ptr1.next
                n2 = ptr2.next
                ptr1.next = ptr2
                ptr2.next = n1
                ptr1 = n1
                ptr2 = n2

        if not head: return head
        h2 = getMid()  # 第二段头节点
        h2 = reverse(h2)  # 逆序
        reorder(head, h2)  # 重排链表

    def reorderListStack(self, head: ListNode) -> None:
        """
        栈存储
        Complexity:
            time: O(NlogN) ? - N为链表节点数
            space: O(N)
        """
        if not head: return head

        stack = []
        h = head.next
        while h:
            stack.append(h)
            h = h.next

        while stack:
            head.next = stack.pop()
            head = head.next
            if stack:
                head.next = stack.pop(0)
                head = head.next
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

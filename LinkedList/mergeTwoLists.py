#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/

21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Complexity:
            time: O(l1+l2)
            space: O(1)
        """
        dummy = ListNode(-1)
        a = dummy
        b = l1
        c = l2
        while b and c:
            if b.val < c.val:
                a.next = b
                b = b.next
            else:
                a.next = c
                c = c.next
            a = a.next
        if b: a.next = b
        if c: a.next = c
        return dummy.next

    def mergeTwoListsIteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Complexity:
            time: O(l1 + l2)
            space: O(l1 + l2)
        """
        if not l1 or not l2: return l2 if not l1 else l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(4)

    node21 = ListNode(1)
    node22 = ListNode(3)
    node23 = ListNode(4)

    node11.next = node12
    node12.next = node13

    node21.next = node22
    node22.next = node23

    s = Solution()
    # res = s.mergeTwoLists(node11, node21)  # 迭代
    res = s.mergeTwoListsIteration(node11, node21)  # 递归
    while res:
        print(res.val, end=' ')
        res = res.next


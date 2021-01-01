#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/partition-list/

86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Complexity:
            time: O(n)
            space: O(1)
        """
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        a = dummy1
        b = dummy2
        c = head
        while c:
            if c.val < x:
                a.next = c
                a = a.next
            else:
                b.next = c
                b = b.next
            c = c.next
        b.next = None
        a.next = dummy2.next  # 连接两个哑节点所在链表
        return dummy1.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    s = Solution()
    res = s.partition(node1, 3)
    while res:
        print(res.val, end=' ')
        res = res.next

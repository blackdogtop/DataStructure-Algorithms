#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/reverse-linked-list/

206. 反转链表
反转一个单链表。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        进栈方法
        Complexity:
            time: O(2n)
            space: O(n)
        """
        if not head: return head

        stack = []
        currentNode = head
        while currentNode:
            stack.append(currentNode.val)
            currentNode = currentNode.next

        dummy = ListNode(-1)
        currentNode = dummy
        while stack:
            currentNode.next = ListNode(stack.pop())
            currentNode = currentNode.next
        return dummy.next

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        双指针方法反转next指针
        Complexity:
            time: O(n)
            space: O(1)
        """
        if not (head and head.next): return head
        pos1 = None
        pos2 = head
        while pos2:
            pos3 = pos2.next
            pos2.next = pos1
            pos1 = pos2
            pos2 = pos3
        return pos1

    def reverseList3(self, head: ListNode) -> ListNode:
        """
        递归
        Complexity:
            time:
            space:
        """
        if not head.next: return head
        last = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    res = s.reverseList(node1)
    # res = s.reverseList2(node1)
    # res = s.reverseList3(node1)
    while res:
        print(res.val, end=' ')
        res = res.next
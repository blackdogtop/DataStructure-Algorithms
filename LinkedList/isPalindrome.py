#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
234. 回文链表

请判断一个链表是否为回文链表。
用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题

输入: 1->2
输出: false
输入: 1->2->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        递归
        Complexity:
            time: ?
            space: O(N/2)
        """
        def recursion(head, last):
            end = head
            while end.next != last:
                end = end.next
            if head.next == end or head.next.next == end:
                if head.val == end.val: return True
                else: return False
            if end.val != head.val: return False
            subListNode = recursion(head.next, end)
            if not subListNode: return False
            return True

        if not head or not head.next: return True
        res = recursion(head, None)
        return res

    def isPalindromeStack(self, head: ListNode) -> bool:
        """
        栈
        Complexity:
            time: O(NlogN)
            space: O(N)
        """
        if not head or not head.next: return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        head, end = stack.pop(0), stack.pop()
        while head is not None and end is not None:
            if head != end: return False
            if stack: head = stack.pop(0)
            if stack: end = stack.pop()
            else: end = None
        return True

    def isPalindromeTwoptrs(self, head: ListNode) -> bool:
        """
        双指针反转前半链表
        Complexity:
            time: O(N)
            space: O(1)
        """
        if not head or not head.next: return True

        # 反转前半链表
        slow, fast = head, head.next
        ptr1 = None
        while fast and fast.next:
            fast = fast.next.next
            ptr2 = slow.next
            slow.next = ptr1
            ptr1 = slow
            slow = ptr2
        ptr2 = slow.next
        slow.next = ptr1
        ptr1 = slow

        if fast is None: ptr1 = ptr1.next  # 奇数链表
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val: return False
            ptr1, ptr2 = ptr1.next, ptr2.next
        return True

    # TODO: 哈希算法(Hash function)


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    # print(s.isPalindrome(node1))  # 递归
    # print(s.isPalindromeStack(node1))  # 栈
    print(s.isPalindromeTwoptrs(node1))  # 双指针

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
            time: O(N)
            space: O(N)
        """
        if not head or not head.next: return True

        lastSec = head  # 倒数第二个节点
        while lastSec.next.next:
            lastSec = lastSec.next
        last = lastSec.next
        lastSec.next = None

        if head.val != last.val: return False
        if not self.isPalindrome(head.next): return False
        return True

    def isPalindromeStack(self, head: ListNode) -> bool:
        """
        栈
        Complexity:
            time: O(N)
            space: O(N)
        """
        if not head or not head.next: return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        begin, end = 0, len(stack)-1
        while begin < end:
            if stack[begin] != stack[end]: return False
            begin += 1
            end -= 1
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

    def isPalindromeReverse(self, head: ListNode) -> bool:
        """
        中断+反转+比较
        Complexity:
            time: O(N)
            space: O(1)
        """
        if not head or not head.next: return True

        slow, fast = head, head.next
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        right = slow.next
        slow.next = None

        pre = None
        while right:
            nex = right.next
            right.next = pre
            pre = right
            right = nex
        right = pre

        while right and head:
            if right.val != head.val: return False
            right = right.next
            head = head.next
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
    print(s.isPalindromeStack(node1))  # 栈
    # print(s.isPalindromeTwoptrs(node1))  # 双指针
    # print(s.isPalindromeReverse(node1))  # 中断+反转+比较

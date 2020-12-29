#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

输入: 1->1->2
输出: 1->2
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        指针 in-place
        Complexity:
            time: O(n)
            space: O(1)
        """
        currentNode = head
        while currentNode and currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head

    def deleteDuplicatesTwoPtrs(self, head: ListNode) -> ListNode:
        """
        双指针
        Complexity:
            time: O(n)
            space: O(1)
        """
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = head, head.next
        while cur:
            while cur and pre.val == cur.val :
                cur = cur.next
            pre.next = cur
            pre = pre.next
            cur = cur.next if cur and cur.next else None
        return dummy.next

    def deleteDuplicatesHash(self, head: ListNode) -> ListNode:
        """
        哈希
        Complexity:
            time: O(n)
            space: O(n)
        """
        if not head: return head

        hash = dict()
        p = head
        while p:
            hash[p.val] = hash[p.val] + 1 if p.val in hash else 1
            p = p.next

        dummy = ListNode(-1)
        pre, cur = dummy, head
        while cur:
            while cur and hash[cur.val] > 1:
                cur = cur.next
                hash[cur.val] -= 1
            pre.next = cur
            cur = cur.next
            pre = pre.next
        return dummy.next

    def deleteDuplicatesRecursion(self, head: ListNode) -> ListNode:
        """
        递归
        Complexity:
            time: O(n)
            space: O(n)
        """
        if not head or not head.next: return head
        sub = self.deleteDuplicatesRecursion(head.next)
        if head.val == sub.val:
            return sub
        else:
            head.next = sub
            return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    s = Solution()
    # res = s.deleteDuplicates(node1)  # in-place
    # res = s.deleteDuplicatesTwoPtrs(node1)  # 双指针
    # res = s.deleteDuplicatesHash(node1)  # hash
    res = s.deleteDuplicatesRecursion(node1)  # 递归
    while res:
        print(res.val, end=' ')
        res = res.next

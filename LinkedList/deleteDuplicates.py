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


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    s = Solution()
    res = s.deleteDuplicates(node1)
    while res:
        print(res.val)
        res = res.next

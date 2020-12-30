#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

输入: 1->2->3->3->4->4->5
输出: 1->2->5
输入: 1->1->1->2->3
输出: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        使用哈希表映射链表重复次数
        Complexity:
            time: O(n)
            space: O(n)
        """
        if not head: return head

        hash = dict()
        currentNode = head
        while currentNode:  # 将重复次数存储到字典中
            if currentNode.val not in hash:
                hash[currentNode.val] = 1
            else:
                hash[currentNode.val] += 1
            currentNode = currentNode.next

        res = ListNode(-1)
        p = res
        for key, value in hash.items():  # 仅添加出现过一次的链表
            if value == 1:
                p.next = ListNode(key)
                p = p.next
        return res.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """
        双指针判断重复
        Complexity:
            time: O(n)
            space: O(1)
        """
        if not (head and head.next): return head
        dummy = ListNode(-1)  # 哑节点
        a = dummy
        a.next = head
        b = head
        while b and b.next:
            if a.next.val != b.next.val:
                a = a.next
                b = a.next
            else:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        return dummy.next

    def deleteDuplicatesRecursion(self, head: ListNode) -> ListNode:
        """
        递归
        Complexity:
            time: O(n)
            space: O(n)
        """
        if not head or not head.next: return head

        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            sub = self.deleteDuplicates(head.next)
            return sub
        else:
            sub = self.deleteDuplicates(head.next)
            head.next = sub
            return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)

    node1.next = node2
    node2.next = node3

    s = Solution()
    # res = s.deleteDuplicates(node1)  # hash
    # res = s.deleteDuplicates2(node1)  # 双指针
    res = s.deleteDuplicatesRecursion(node1)  # 递归
    while res:
        print(res.val, end=' ')
        res = res.next

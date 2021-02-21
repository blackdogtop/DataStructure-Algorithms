# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

输入：head = [1,3,2]
输出：[2,3,1]
"""


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        """
        辅助stack
        Complexity:
            time: O(n)
            space: O(n)
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    def reversePrintReversion(self, head: ListNode) -> List[int]:
        """
        递归
        Complexity:
            time: O(n)
            space: O(n)
        """
        return self.reversePrintReversion(head.next) + [head.val] if head else []


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    s = Solution()
    # res = s.reversePrint(node1)  # stack
    res = s.reversePrintReversion(node1)  # 递归
    print(res)

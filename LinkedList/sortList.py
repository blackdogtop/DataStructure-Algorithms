#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/sort-list/

148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序

输入：head = [4,2,1,3]
输出：[1,2,3,4]

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

输入：head = []
输出：[]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        merge sort 归并排序
        Complexity:
            time: O(NlogN) ?
            space: O(logN)
        """
        if not head or not head.next: return head

        # 获取链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None

        dummy = ListNode(-1)
        p = dummy
        # 递归
        left = self.sortList(head)
        right = self.sortList(mid)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next

    def sortListIteration(self, head: ListNode) -> ListNode:
        """
        Complexity:
            time: O(NlogN)
            space: O(1)
        """

        def getHead(node, step):
            """获取节点step个步长后的节点"""
            if not node: return None
            for _ in range(step, 1, -1):
                if node and node.next: node = node.next
            right = node.next
            node.next = None  # 将与上一个部分的next指针置空
            return right

        def mergeSort(h1, h2):
            """
            归并排序两个链表至res
            :param h1, h2: 两个链表的头节点
            """
            nonlocal res
            while h1 and h2:
                if h1.val < h2.val:
                    res.next = h1
                    h1 = h1.next
                else:
                    res.next = h2
                    h2 = h2.next
                res = res.next
            res.next = h1 if h1 else h2
            while res.next: res = res.next  # res置尾

        if not head: return head

        length, h = 0, head
        while h: length, h = length + 1, h.next  # 链表长度

        dummy = ListNode(-1)
        res = dummy
        res.next = head

        step = 1
        while step < length:
            cur = res.next
            while cur:
                h1 = cur  # 第一部分头节点
                h2 = getHead(h1, step)  # 第二部分头节点
                cur = getHead(h2, step)  # 更新下一次的第一部分头节点
                mergeSort(h1, h2)
            res = dummy
            step *= 2

        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(0)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    # res = s.sortList(node1)  # 迭代
    res = s.sortListIteration(node1)  # 递归
    while res:
        print(res.val, end=' ')
        res = res.next

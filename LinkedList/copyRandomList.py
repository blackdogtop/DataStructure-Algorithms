#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的深拷贝。
我们用一个由n个节点组成的链表来表示输入/输出中的链表。每个节点用一个[val, random_index]表示：
val：一个表示Node.val的整数。
random_index：随机指针指向的节点索引（范围从0到n-1）；如果不指向任何节点，则为null。

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Complexity:
            time: O(n)
            space: O(1)
        """
        if not head: return head

        # 在原节点后创建节点
        p = head
        while p:
            newNode = Node(p.val, None, None)
            newNode.next = p.next
            p.next = newNode
            p = p.next.next

        # 赋值随机节点
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # 分离两个链表
        dummy = Node(-1, None, None)
        cur = dummy
        p = head
        while p:
            cur.next = p.next
            p = p.next.next
            cur = cur.next
        return dummy.next

    def copyRandomListHash(self, head: 'Node') -> 'Node':
        """
        哈希
        Complexity:
            time: O(n)
            space: O(n)
        """
        if not head: return head

        hash = dict()  # 原节点 : 新节点
        p = head
        while p:
            hash[p] = Node(p.val, None, None)
            p = p.next

        p = head
        while p:
            if p.next:
                hash[p].next = hash[p.next]
            if p.random:
                hash[p].random = hash[p.random]
            p = p.next

        return hash[head]


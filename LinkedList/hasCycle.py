#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
141. 环形链表

给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
用 O(1)（即，常量）内存解决此问题吗

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Complexity:
            time: O(N)?
            space: O(N)
        """
        stack = []
        while head:
            if head not in stack:
                stack.append(head)
            else:
                return True
            head = head.next
        return False

    def hasCycleReverse(self, head: ListNode) -> bool:
        """
        逆序法 - 从头节点开始逆序链表中所有节点，当current的p2节点==头节点时 则回到了头节点 说明链表有环
        Complexity:
            time: O(N)
            space: O(1)
        """
        if not head: return False
        p1 = None
        p2 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            if p2 == head: return True  # 当逆序后链表的p2与头节点相同说明回到了头节点 则链表有环
        return False

    def hasCycleTwoPtr(self, head: ListNode) -> bool:
        """
        快慢双指针 - 当两指针相遇则说明有环
        Complexity:
            time: O(N)
            space: O(1)
        """
        if not head: return False
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False


if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    s = Solution()
    # print(s.hasCycle(node1))  # 栈方法
    # print(s.hasCycleReverse(node1))  # 逆序方法
    print(s.hasCycleTwoPtr(node1))  # 双指针

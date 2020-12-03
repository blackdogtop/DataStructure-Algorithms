#!usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Complexity:
            time: O(n)
            space: O(2n)
        :param root: TreeNode
        :return res: list
        """
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        """
        Complexity:
            time: O(n)
            space: O(n)
        :param root: TreeNode
        :return res: list
        """
        res = []

        def dfs(root: TreeNode):
            nonlocal res
            if not root: return
            if root.left: dfs(root.left)
            res.append(root.val)
            if root.right: dfs(root.right)

        dfs(root)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    s = Solution()
    res = s.inorderTraversal(node1)
    print(res)

    res2 = s.inorderTraversalRecursion(node1)
    print(res2)

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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Complexity:
            time: O(n)
            space: O(2n)
        :param root: TreeNode
        :return res: list
        """
        stack = []  # use a stack to store tree node
        res = []  # a list to store result
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                root = root.right
        return res

    def preorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        """
        Complexity:
            time: O(n)
            space: O(n)
        :param root:
        :return res: list
        ref: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/
        """
        res = []

        def dfs(root):
            nonlocal res  # 更改res作用域使其在外层函数操作
            if not root: return
            res.append(root.val)
            if root.left: dfs(root.left)
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
    res = s.preorderTraversal(node1)
    print(res)

    res2 = s.preorderTraversalRecursion(node1)
    print(res2)

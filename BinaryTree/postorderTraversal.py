#!usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
"""
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

输入: [1,null,2,3]
输出: [3,2,1]
"""


class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
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
                root = root.left if root.left else root.right
            root = stack.pop()
            res.append(root.val)
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                root = None
        return res

    def postorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        """
        Complexity:
            time: O(n)
            space: O(2n)
        :param root: TreeNode
        :return res: list
        """
        res = []

        def dfs(root: TreeNode):
            nonlocal res
            if not root: return
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    s = Solution()
    res = s.postorderTraversal(node1)
    print(res)

    res2 = s.postorderTraversalRecursion(node1)
    print(res2)
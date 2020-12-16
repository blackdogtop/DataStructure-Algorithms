#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

二叉树：[3,9,20,null,null,15,7],
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        stack = [root]
        while stack:
            size = len(stack)
            layer = []
            while size > 0:
                currentNode = stack.pop(0)
                if currentNode.left: stack.append(currentNode.left)
                if currentNode.right: stack.append(currentNode.right)
                layer.append(currentNode.val)
                size -= 1
            res.append(layer)
        return res


if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7

    s = Solution()
    res = s.levelOrder(node3)
    print(res)

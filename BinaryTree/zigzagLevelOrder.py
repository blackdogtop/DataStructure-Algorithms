#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树[3,9,20,null,null,15,7],
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Complexity:
            time: O(NlogN) - list.reverse时间复杂度为(n)
            space:  ?
        """
        res = []
        layerNum = 0
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
            if layerNum % 2 != 0: layer.reverse()  # .reverse()相比于[::-1]不会创建新的内存空间
            res.append(layer)
            layerNum += 1
        return res


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    s = Solution()
    res = s.zigzagLevelOrder(node1)
    print(res)

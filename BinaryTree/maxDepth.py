#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

104. 二叉树的最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Complexity:
            time: O(n)
            space: O(height) - height为二叉树的最大深度 函数递归需要栈空间 栈空间取决于递归次数
        """
        if not root: return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1

    def bfs(self, root: TreeNode):
        """
        Complexity:
            time: 最坏O(n * n)? - pop(0)占用O(n)的时间复杂度
            space: 最坏O(n)
        """
        if not root: return 0
        stack = [root]
        layer = 0
        while stack:
            size = len(stack)
            while size > 0:
                currentNode = stack.pop(0)
                if currentNode.left: stack.append(currentNode.left)
                if currentNode.right: stack.append(currentNode.right)
                size -= 1
            layer += 1
        return layer


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
    res = s.maxDepth(node3)
    print(res)

    res2 = s.bfs(node3)
    print(res2)



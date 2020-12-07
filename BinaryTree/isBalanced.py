#!usr/bin/env python
# -*- coding: utf-8 -*-
import math
"""
https://leetcode-cn.com/problems/balanced-binary-tree/

110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

输入：root = [3,9,20,null,null,15,7]
输出：true
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
输入：root = []
输出：true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Complexity:
            time: O(NlogN) - 广度优先O(N) 最大深度O(logN)
            space: 最坏O(n)
        """
        def maxDepth(root: TreeNode):
            """
            以root为根结点的二叉树最大高度
            complexity:
                time: O(logN)
                space: O(1)
            """
            if not root: return 0
            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            return max(leftDepth, rightDepth) + 1

        # 广度优先
        if not root: return True
        stack = [root]
        while stack:
            currentNode = stack.pop()
            leftDepth = maxDepth(currentNode.left)
            rightDepth = maxDepth(currentNode.right)
            if abs(leftDepth - rightDepth) > 1: return False

            if currentNode.left: stack.append(currentNode.left)
            if currentNode.right: stack.append(currentNode.right)
        return True

    def isBalancedOptimised(self, root: TreeNode) -> bool:
        """
        Complexity:
            time: O(n)
            space: O(1)
        """
        def maxDepth(root: TreeNode):
            """
            在平衡树的条件下以root为根结点的二叉树最大深度
            :return depth: 如果是平衡树则返回该节点的最大深度 否则返回-1
            """
            if not root: return 0
            # 获取左右子树深度并判断是否平衡
            leftDepth = maxDepth(root.left)
            if leftDepth == -1: return -1
            rightDepth = maxDepth(root.right)
            if rightDepth == -1: return -1
            return max(leftDepth, rightDepth) + 1 if abs(leftDepth - rightDepth) <= 1 else -1

        if not root: return True
        if maxDepth(root) == -1: return False
        return True


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
    res = s.isBalanced(node3)
    print(res)

    res2 = s.isBalancedOptimised(node3)
    print(res2)







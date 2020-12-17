#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/validate-binary-search-tree/

98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

输入:
    2
   / \
  1   3
输出: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Complexity:
            time: O(n)
            space: O(n)
        """
        def bst(root: TreeNode, leftMax, rightMin):
            if not root: return True
            left = bst(root.left, leftMax, root.val)
            if not left: return False
            right = bst(root.right, root.val, rightMin)
            if not right: return False
            if left and right and (leftMax < root.val < rightMin):
                return True
            return False

        leftMax, rightMin = float('-inf'), float('inf')
        res = bst(root, leftMax, rightMin)
        return res


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(6)
    node4 = TreeNode(3)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    s = Solution()
    res = s.isValidBST(node1)
    print(res)

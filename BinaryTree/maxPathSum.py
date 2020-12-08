#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

124. 二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

输入：[1,2,3]
输出：6
输入：[-10,9,20,null,null,15,7]
输出：42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def recursion(root: TreeNode):
            """
            当root为根结点的左/右子树最大路径和
            Complexity:
                time: O(N)
                space: 最坏O(N)
            """
            if not root: return 0
            left = recursion(root.left)
            right = recursion(root.right)

            # 更新最大值
            nonlocal maxSum
            if root.val + max(left, 0) + max(right, 0) > maxSum: maxSum = root.val + max(left, 0) + max(right, 0)

            return max(0, left, right) + root.val

        maxSum = float("-inf")
        recursion(root)
        return maxSum


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(11)
    node3 = TreeNode(7)
    node4 = TreeNode(2)

    node1.left = node2
    node2.left = node3
    node2.right = node4

    s = Solution()
    res = s.maxPathSum(node1)
    print(res)




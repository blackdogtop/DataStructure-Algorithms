#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/

701. 二叉搜索树中的插入操作
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Complexity:
            time: O(logN)
            space: O(1)
        """
        if not root: return TreeNode(val)
        pos = root
        while pos:
            if pos.val < val:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right
            elif pos.val > val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left
        return root


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    s = Solution()
    s.insertIntoBST(node1, 4)
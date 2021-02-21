# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归
        Complexity:
            time: O(N) - N为树的节点数
            space: O(N) - N为树的节点数(树的深度h小于节点数N, 故为N)
        """
        if not preorder: return
        root = TreeNode(preorder[0])
        rootIndexInorder = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:rootIndexInorder+1], inorder[:rootIndexInorder])
        root.right = self.buildTree(preorder[rootIndexInorder+1:], inorder[rootIndexInorder+1:])
        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    res = s.buildTree(preorder, inorder)
    print(res.val)
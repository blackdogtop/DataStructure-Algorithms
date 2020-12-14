#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Complexity:
            time: O(NlogN)
            space: 最差O(2N)
        """
        def dfs(root: TreeNode, target: TreeNode):
            """
            深度优先遍历判断节点target是否在以root为根的树中
            Complexity:
                time: O(n) - n为节点数
                space: 最差O(2n)
            """
            if not root: return
            stack = []
            while root or stack:
                while root:
                    if root == target: return True
                    stack.append(root)
                    root = root.left
                if stack:
                    root = stack.pop()
                    root = root.right
            return False

        while root:
            if root == p or root == q: return root
            # p / q是否在root的左子树
            pInLeft = dfs(root.left, p)
            qInLeft = dfs(root.left, q)
            if (qInLeft and not pInLeft) or (not qInLeft and pInLeft):  # pq在root异侧
                return root
            if (qInLeft and pInLeft) or (not qInLeft and not pInLeft):  # pq在root同侧
                if (qInLeft and pInLeft):
                    root = root.left
                else:
                    root = root.right

    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Complexity:
            time: O(n)
            space: 最差O(n)
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)
        if not left: return right
        if not right: return left
        if left and right:  # p q在异侧
            return root


if __name__ == '__main__':
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node4 = TreeNode(4)

    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    node2.left = node7
    node2.right = node4

    p = node5
    q = node1

    s = Solution()
    res = s.lowestCommonAncestor(node3, p, q)
    res1 = s.lowestCommonAncestor1(node3, p, q)
    print(res.val, res1.val)


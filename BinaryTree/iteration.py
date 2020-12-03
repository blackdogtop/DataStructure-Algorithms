#!usr/bin/env python
# -*- coding: utf-8 -*_

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Iteration:
    def preOrder(self, root: Tree):
        """pre-order: root - left - right"""
        if not root: return
        print(root.data, end=' ')
        if root.left: self.preOrder(root.left)
        if root.right: self.preOrder(root.right)

    def preOrderNonRecursion(self, root: Tree):
        """non-recussion pre-order"""
        stack = []  # used a stack to store result
        while root or stack:
            while root:
                print(root.data, end=' ')
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                root = root.right

    def inOrder(self, root: Tree):
        """in-order: left - root - right"""
        if not root: return
        if root.left: self.inOrder(root.left)
        print(root.data, end=' ')
        if root.right: self.inOrder(root.right)

    def inOrderNonRecursion(self, root: Tree):
        """non-recursion in-order"""
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                print(root.data, end=' ')
                root = root.right

    def postOrder(self, root: Tree):
        """post-order: left - right - root"""
        if not root: return
        if root.left: self.postOrder(root.left)
        if root.right: self.postOrder(root.right)
        print(root.data, end=' ')

    def postOrderNonRecursion(self, root: Tree):
        """non-recursion post-order"""
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right
            root = stack.pop()
            print(root.data, end=' ')
            if stack and stack[-1].left == root:  # 输出左子树的条件下将root置为右子树
                root = stack[-1].right
            else:
                root = None  # 输出又子树的条件下将root置为None


if __name__ == '__main__':
    node1 = Tree(1)
    node2 = Tree(2)
    node3 = Tree(3)
    node4 = Tree(4)
    node5 = Tree(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    i = Iteration()

    # recursion
    i.preOrder(node1)
    i.inOrder(node1)
    i.postOrder(node1)

    # non-recursion
    i.preOrderNonRecursion(node1)
    i.inOrderNonRecursion(node1)
    i.postOrderNonRecursion(node1)
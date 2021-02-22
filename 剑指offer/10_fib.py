# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
F(0) = 0, F(1)= 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

输入：n = 2
输出：1
输入：n = 5
输出：5
"""
from functools import lru_cache


class Solution:
    def __init__(self):
        self.fibDic = {}

    def fib(self, n: int) -> int:
        """
        递归
        Complexity:
            time: O(2^n) - n为类二叉树节点数
            space: O(n) - n为类二叉树高度
        """
        if n in self.fibDic: return self.fibDic[n]
        if n < 2: return n
        value = int((self.fib(n-1) + self.fib(n-2)) % (1e9+7))
        self.fibDic[n] = value
        return value

    @lru_cache()
    def fibDectorate(self, n: int) -> int:
        """
        递归
        Complexity:
            time: O(2^n) - n为类二叉树节点数
            space: O(n) - n为类二叉树高度
        """
        if n < 2: return n
        return int((self.fib(n-1) + self.fib(n-2)) % (1e9+7))

    def fibDynamicProgramming(self, n: int) -> int:
        """
        动态规划
        Complexity:
            time: O(n)
            space: O(1)
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007


if __name__ == "__main__":
    n = 81
    s = Solution()
    # res = s.fib(n)
    # res = s.fibDectorate(n)
    res = s.fibDynamicProgramming(n)
    print(res)

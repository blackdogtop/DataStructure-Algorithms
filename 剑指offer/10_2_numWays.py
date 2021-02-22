# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

输入：n = 2
输出：2
输入：n = 7
输出：21
输入：n = 0
输出：1
"""
from functools import lru_cache


class Solution(object):
    def __init__(self):
        self.waysDict = {}

    @lru_cache()
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n < 3: return n
        return (self.numWays(n-2) + self.numWays(n-1)) % 1000000007

    def numWaysDict(self, n):
        if n in self.waysDict: return self.waysDict[n]
        if n == 0: return 1
        if n < 3: return n
        res = (self.numWaysDict(n-1) + self.numWaysDict(n-2)) % 1000000007
        self.waysDict[n] = res
        return res

    def numWaysDP(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007


if __name__ == "__main__":
    n = 10
    s = Solution()
    # res = s.numWays(n)  # 递归
    # res = s.numWaysDict(n)  # 字典
    res = s.numWaysDP(n)  # DP
    print(res)

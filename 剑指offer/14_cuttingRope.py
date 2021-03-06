# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/


给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36
"""
import math
from functools import lru_cache


class Solution:
    def __init__(self):
        self.dict = {}

    def cuttingRope(self, n: int) -> int:
        """
        数学推导
        Complexity:
            time: O(1)
            space: O(1)
        """
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    def cuttingRopeRecursion(self, n: int) -> int:
        """
        暴力递归
        Complexity:
            time: O(2^N)
            space: O(N)
        """
        if n == 2: return 1
        if n in self.dict: return self.dict[n]
        res = -1
        for i in range(1, n + 1):
            res = max(res, max(i * self.cuttingRope(n - i), i * (n - i)))
        self.dict[n] = res
        return res

    @lru_cache()
    def cuttingRopeRecursion1(self, n: int) -> int:
        """
        暴力递归(同上)
        Complexity:
            time: O(2^N)
            space: O(2^N)
        """
        if n == 2: return 1
        res = -1
        for i in range(1, n + 1):
            res = max(res, max(i * self.cuttingRope(n - i), i * (n - i)))
        return res

    def cuttingRopeDP(self, n: int) -> int:
        """
        动态规划
        Complexity:
            time:
            space:
        """
        dp = [0 for _ in range(n + 1)]  # 长度为i的绳子乘积最大值
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * (i - j))
        return dp[n]


if __name__ == "__main__":
    n = 10
    s = Solution()
    # res = s.cuttingRope(n)
    # res = s.cuttingRopeRecursion(n)
    # res = s.cuttingRopeRecursion1(n)
    res = s.cuttingRopeDP(n)
    print(res)

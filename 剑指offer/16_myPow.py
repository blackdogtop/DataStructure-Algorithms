# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题

输入: 2.00000, 10
输出: 1024.00000
输入: 2.10000, 3
输出: 9.26100
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Complexity:
            time: O(n)
            space: O(1)
        """
        if x == 0: return 0
        res = 1
        if n < 1: x, n = 1/x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.myPow(3, 5)
    print(res)

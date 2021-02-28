# -*- coding: utf-8 -*-
"""
请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。
例如，把 9表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011中，共有三位为 '1'。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Complexity:
            time: O(log2 n)
            space: O(1)
        :param n:
        :return:
        """
        res = 0
        while n:
            if n & 1: res += 1
            n = n >> 1  # 右移运算符
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(1))

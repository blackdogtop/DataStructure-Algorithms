#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/implement-strstr/

28. 实现 strStr()
给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回-1

输入: haystack = "hello", needle = "ll"
输出: 2
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Iterate haystack and judge equation
        complexity:
            time: O((n-l)l)     n - len(haystack) l - len(needle)
            space: O(1)
        """
        def isEqual(haystack: str, needle: str) -> bool:
            """time complexity: O(n)"""
            if len(haystack) != len(needle): return False
            for i in range(len(haystack)):
                if haystack[i] != needle[i]: return False
            return True

        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle: return i  # 判断相等占用len(needle)时间复杂度
            # if isEqual(haystack[i:i + len(needle)], needle): return i # 字符串比较也就是isEqual函数
        return -1

    def kmp(self, haystack: str, needle: str) -> int:
        """
        Knuth–Morris–Pratt algorithm
        complexity:
            time:
            space:
        ref: https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
        """
        pass  # TODO: kmp algorithm


if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    s = Solution()
    res = s.strStr(haystack, needle)
    print(res)
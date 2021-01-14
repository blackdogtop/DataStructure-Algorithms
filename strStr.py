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
        逐一比较子字符串
        complexity:
            time: O((m-n)n)     m - len(haystack) n- len(needle)
            space: O(1)
        """
        def isEqual(haystack: str, needle: str) -> bool:
            """time complexity: O(n)"""
            haystackLength = len(haystack)
            for i in range(haystackLength):
                if haystack[i] != needle[i]:
                    return False
            return True

        m = len(haystack)
        n = len(needle)
        for i in range(0, m - n + 1):
            if isEqual(haystack[i: i + n], needle):
                return i
        return -1

    def strStrTwoPtrs(self, haystack: str, needle: str) -> int:
        """
        双指针
        Complexity:
            time: O((m-n)n) - 最差
            space: O(1)
        """
        if not needle: return 0
        if not haystack: return -1
        m = len(haystack)
        n = len(needle)
        i = 0
        while i < m:
            if haystack[i] == needle[0]:
                equalNum = 0  # 相同元素数
                j = 0
                index = i
                while j < n and i < m:
                    if haystack[i] != needle[j]:
                        i = i - equalNum + 1  # 移动指针i至当前位置与相同元素数加一
                        break
                    if j == n - 1:
                        return index
                    equalNum += 1
                    i += 1
                    j += 1
            else:
                i += 1
        return -1


if __name__ == '__main__':
    haystack = 'mississippi'
    needle = 'issip'
    s = Solution()
    # res = s.strStr(haystack, needle)  # 逐一比较子字符串
    res = s.strStrTwoPtrs(haystack, needle)  # 双指针
    print(res)

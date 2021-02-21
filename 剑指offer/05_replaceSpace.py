# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."
输出："We%20are%20happy."
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return "%20".join(s.split(" "))


if __name__ == "__main__":
    s = "We are happy."
    solution = Solution()
    res = solution.replaceSpace(s)
    print(res)

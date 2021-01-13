# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/decode-string/

394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

输入：s = "3[a]2[bc]"
输出："aaabcbc"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Stack
        Complexity:
            time: O(n)
            space: O(n) - 最差
        """
        res = ""
        stack = []  # a stack is used to store last res and current multiplier
        multiply = 0
        for cur in s:
            if cur.isdigit():
                multiply = multiply * 10 + int(cur)
            elif cur == '[':
                stack.append([multiply, res])
                res, multiply = "", 0
            elif cur == ']':
                curMulti, lastRes = stack.pop()
                res = lastRes + curMulti * res
            else:
                res += cur
        return res

    def decodeStringRecursion(self, s: str) -> str:
        """
        使用递归返回方括号内的string
        Complexity:
            time: O(n)
            space: O(n) - 最差
        """
        def recursion(s, i):
            """
            :param s: str
            :param i: index
            """
            res, multi = "", 0
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    temp, i = recursion(s, i + 1)
                    res = res + multi * temp
                    multi = 0
                elif s[i].isalpha():
                    res += s[i]
                else:
                    return res, i
                i += 1
            return res

        return recursion(s, 0)


if __name__ == '__main__':
    string = "3[a2[b]]"
    s = Solution()
    print(s.decodeString(string))  # stack
    print(s.decodeStringRecursion(string))  # recursion

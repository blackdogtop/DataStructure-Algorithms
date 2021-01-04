# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

根据 逆波兰表示法，求表达式的值。
有效的运算符包括+,-,*,/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Complexity:
            time: O(n)
            space: O(n) - 最差
        """
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit(): stack.append(token)
            else:
                n1, n2 = stack.pop(), stack.pop()
                stack.append(str(int(eval(n2 + token + n1))))
        return int(stack[-1])


if __name__ == '__main__':
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))
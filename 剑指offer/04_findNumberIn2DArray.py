# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。
给定target=20，返回false。
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        '在右上角看, 这个矩阵其实就像是一个Binary Search Tree'
        Complexity:
            time: 最差O(m+n)
            space: O(1)
        """
        if not matrix or not matrix[0]: return False
        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        rows, columns = len(matrix), len(matrix[0])
        row, column = 0, columns-1
        root = matrix[row][column]
        while True:
            if target == root: return True
            elif target < root:
                if column-1 >= 0: column -= 1
                else: return False
            elif target > root:
                if row+1 < rows: row += 1
                else: return False
            root = matrix[row][column]


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
    s = Solution()
    print(s.findNumberIn2DArray(matrix, 20))

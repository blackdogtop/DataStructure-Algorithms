# -*- coding: utf-8 -*-
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Complexity:
            time: 最差O(4^K MN) - K为word长度 MN为矩阵行列大小
            space: 最差O(MN)
        """
        def dfs(i, j, wordIndex, used):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return False
            if board[i][j] != word[wordIndex] or used[i][j]: return False
            used[i][j] = 1
            if wordIndex == len(word) - 1: return True
            res = dfs(i + 1, j, wordIndex + 1, used) or dfs(i, j + 1, wordIndex + 1, used) or dfs(i - 1, j, wordIndex + 1, used) or dfs(i, j - 1, wordIndex + 1, used)
            used[i][j] = 0
            return res

        used = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, used): return True
        return False


if __name__ == "__main__":
    board = [["A","C","E"],["D","E","S"]]
    word = 'CESED'
    s = Solution()
    print(s.exist(board, word))

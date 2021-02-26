# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

输入：m = 2, n = 3, k = 1
输出：3
输入：m = 3, n = 1, k = 0
输出：1
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        动态规划
        Complexity:
            time: O(MN)
            space: O(MN)
        """
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(min(m, 10)):
            if i <= k:
                dp[i][0] = 1
                res += 1
        for j in range(1, min(n, 10)):
            if j <= k:
                dp[0][j] = 1
                res += 1

        for i in range(m):
            for j in range(n):
                if dp[i][j]: continue
                if (dp[i - 1][j] or dp[i][j - 1]) and (i // 10 + i % 10) + (j // 10 + j % 10) <= k:
                    dp[i][j] = 1
                    res += 1
        return res

    def movingCountDFS(self, m: int, n: int, k: int) -> int:
        """
        深度优先搜索
        Complexity:
            time: O(MN)
            space: O(MN)
        """

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= m or j >= n: return 0
            if visited[i][j] or (i // 10 + i % 10) + (j // 10 + j % 10) > k: return 0
            visited[i][j] = 1
            return dfs(i + 1, j, visited) + dfs(i - 1, j, visited) + dfs(i, j + 1, visited) + dfs(i, j - 1, visited) + 1

        return dfs(0, 0, [[0 for _ in range(n)] for _ in range(m)])

    def movingCountBFS(self, m: int, n: int, k: int) -> int:
        """
        广度优先搜索
        Complexity:
            time: O(MN)
            space: O(MN)
        """
        queue, visited = [(0, 0)], set()
        while queue:
            i, j = queue.pop(0)
            if (i, j) not in visited and 0 <= i < m and 0 <= j < n and (i // 10 + i % 10) + (j // 10 + j % 10) <= k:
                visited.add((i, j))
                for si, sj in [(i+1, j), (i, j+1)]: queue.append((si, sj))
        return len(visited)



if __name__ == "__main__":
    m, n, k = 2, 3, 1
    s = Solution()
    # res = s.movingCount(m, n, k)  # 动态规划
    # res = s.movingCountDFS(m, n, k)  # 深度优先搜索
    res = s.movingCountBFS(m, n, k)  # 广度优先搜索
    print(res)

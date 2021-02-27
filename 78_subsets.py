#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/subsets/

78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

输入: nums = [1,2,3]
输出:
[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
"""
from typing import List


class Solution:
    """更简单的方法可参考 https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        back track algorithm
        complexity:
            time: O(2^n)
            space: O(3n) ?
        """

        def backTrack(nums: list, path: list, res: list, begin: int):
            res.append(path[:])  # shallow copy, without change any thing when the path append/pop element
            # if len(path) == len(nums): return
            for i in range(begin, len(nums)):
                path.append(nums[i])

                backTrack(nums, path, res, i + 1)

                path.pop()

        res = []
        backTrack(nums, [], res, 0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    res = s.subsets(nums)
    print(res)

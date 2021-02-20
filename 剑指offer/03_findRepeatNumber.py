# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        hash
        Complexity:
            time: 最差O(n)
            space: 最差O(n)
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                return i

    def findRepeatNumberSort(self, nums: List[int]) -> int:
        """
        heap sort
        Complexity:
            time: 最差O(NlogN)
            space: O(1)
        """
        nums = self.heapSort(nums)
        for i, num in enumerate(nums):
            if num == nums[i+1]:
                return num

    def heapSort(self, nums):
        def siftDown(start, end):
            """最大堆调整"""
            nonlocal nums
            root = start
            while True:
                child = root * 2 + 1
                if child > end:
                    break
                if child + 1 <= end and nums[child] < nums[child+1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break

        # 创建最大堆
        for start in range(len(nums) // 2 - 1, -1, -1):
            siftDown(start, len(nums) - 1)
        # 堆排序
        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            siftDown(0, end-1)
        return nums

    def findRepeatNumberHashInPlace(self, nums: List[int]) -> int:
        """
        原地哈希
        Complexity:
            time: 最差O(n)
            space: O(1)
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]  # 将第i位的值放在应有的索引下


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    # res = s.findRepeatNumber(nums)  # hash
    # res = s.findRepeatNumberSort(nums)  # heap sort
    res = s.findRepeatNumberHashInPlace(nums)  # 原地hash
    print(res)

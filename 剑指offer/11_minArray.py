# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

输入：[3,4,5,1,2]
输出：1
输入：[2,2,2,0,1]
输出：0
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        Complexity:
            time: 最差O(n)
            space: O(1)
        """
        res = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < res:
                return numbers[i]
        return res

    def minArrayBinarySearch(self, numbers):
        """
        折半查找
        Complexity:
            time: O(NlogN)
            space: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1  # 去重
        return numbers[left]

    def minArrayDivide(self, numbers):
        """
        分治法
        Complexity:
            time: O(NlogN)
            space: O(NlogN)?
        """
        def divideMethod(nums, left, right):
            if left + 1 >= right: return min(nums[left], nums[right])
            if nums[left] < nums[right]: return nums[left]
            mid = (left + right) // 2
            return min(divideMethod(nums, left, mid - 1), divideMethod(nums, mid, right))
        return divideMethod(numbers, 0, len(numbers)-1)


if __name__ == "__main__":
    numbers = [3,4,5,1,2]
    s = Solution()
    # res = s.minArray(numbers)
    # res = s.minArrayBinarySearch(numbers)  # 折半查找
    res = s.minArrayDivide(numbers)  # 分治法
    print(res)

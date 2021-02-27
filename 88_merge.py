# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/merge-sorted-array/

给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        双指针
        Complexity:
            time: O(m + n)
            space: 最好 O(m)
        """
        nums1Copy = nums1[:m]
        nums1[:] = []

        i, j = 0, 0
        while i < m and j < n:
            if nums1Copy[i] < nums2[j]:
                nums1.append(nums1Copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i == m:
            nums1.extend(nums2[j:])
        if j == n:
            nums1.extend(nums1Copy[i:])
        print(nums1)

    def mergeSort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Complexity:
            time: O(nm) ?
            space: O(m) ?
        """
        nums1[:] = nums1[:m]
        if m == 0:
            nums1[:] = nums2
            nums2 = []
        while nums2:
            nums1.append(nums2.pop(0))
            i = -1
            while i >= 1 - len(nums1) and nums1[i-1] > nums1[i]:
                nums1[i-1], nums1[i] = nums1[i], nums1[i-1]
                i -= 1
        print(nums1)

    def mergePtrs(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        双指针
        Complexity:
            time: O(m + n)
            space: O(1)
        """
        p1, p2 = m-1, n-1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(nums1)



if __name__ == "__main__":
    s = Solution()
    # s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    # s.mergeSort(nums1 = [2, 0], m = 1, nums2 = [1], n = 1)
    s.mergePtrs(nums1 = [2, 0], m = 1, nums2 = [1], n = 1)

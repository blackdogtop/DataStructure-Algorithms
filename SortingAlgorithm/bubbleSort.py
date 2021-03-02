# -*- coding: utf-8 -*-


def bubbleSort(nums: list):
    """
    Complexity:
        time: O(n^2)
        space: O(1)
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__":
    nums = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
    res = bubbleSort(nums)
    print(res)

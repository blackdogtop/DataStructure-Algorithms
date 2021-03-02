# -*- coding: utf-8 -*-


def selectionSort(nums: list):
    """
    Complexity:
        time: O(n^2)
        space: O(1)
    """
    for i in range(len(nums) - 1):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[minIndex] > nums[j]:
                minIndex = j
        if i == minIndex:
            pass
        else:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


if __name__ == "__main__":
    nums = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    res = selectionSort(nums)
    print(res)

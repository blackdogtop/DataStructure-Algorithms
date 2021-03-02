# -*- coding: utf-8 -*-


def insertionSort(nums: list):
    """
    Complexity:
        time: O(n^2)
        space: O(1)
    """
    for i in range(1, len(nums)):
        j = i - 1
        current = nums[i]
        while j >= 0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums


if __name__ == "__main__":
    nums = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    res = insertionSort(nums)
    print(res)

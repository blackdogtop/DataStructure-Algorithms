# -*- coding: utf-8 -*-


def quickSort(nums: list):
    """
    Complexity:
        time: 平均O(NlogN) 最差O(N^2)
        space: O(logN)
    """
    if len(nums) < 2: return nums

    pivot = nums[0]
    j = 0
    for i in range(1, len(nums)):
        if nums[i] <= pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[j], nums[0] = nums[0], nums[j]

    left = nums[:j]
    right = nums[j+1:]
    return quickSort(left) + [nums[j]] + quickSort(right)


if __name__ == "__main__":
    nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    res = quickSort(nums)
    print(res)

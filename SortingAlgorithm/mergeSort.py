# -*- coding: utf-8 -*-


def mergeSort(nums: list):
    """
    Complexity:
        time: O(NlogN)
        space: O(N)
    """
    if len(nums) < 2: return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res


if __name__ == "__main__":
    nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    res = mergeSort(nums)
    print(res)

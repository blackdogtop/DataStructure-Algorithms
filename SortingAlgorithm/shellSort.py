# -*- coding: utf-8 -*-


def shellSort(nums: list):
    """
    Complexity:
        time: O(N log^2 N)
        space: O(1)
    """
    gap = len(nums)//2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i
            while j >= 0 and j - gap >= 0 and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap//2
    return nums


if __name__ == "__main__":
    nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    res = shellSort(nums)
    print(res)

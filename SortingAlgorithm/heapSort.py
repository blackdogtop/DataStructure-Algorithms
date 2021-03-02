# -*- coding: utf-8 -*-


def heapSort(nums: list):
    """
    Complexity:
        time: O(NlogN)
        space: O(1)
    """
    def siftDown(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child+1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
            else:
                break
    # 创建最大堆
    for start in range(len(nums)//2 - 1, -1, -1):
        siftDown(start, len(nums)-1)
    # 堆排序
    for end in range(len(nums)-1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        siftDown(0, end-1)
    return nums


if __name__ == "__main__":
    nums = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    res = heapSort(nums)
    print(res)

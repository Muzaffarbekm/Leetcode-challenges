# 35. Search Insert Position | Leetcode.com

# Given a sorted array of distinct integers and a target value, return the index if the 
# target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1

        all = (low + high) // 2
        if low > all:
            return low
        else:
            return high - 1 
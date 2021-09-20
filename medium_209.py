'''Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn’t one, return 0 instead.  => s = 7, nums = [2,3,1,2,4,3]  => Output: 2

I used  Sliding Window Algorithm to solve it.
'''

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
     
        start = 0
        res = float('inf')
        carry_sum = 0
        
        for i, num in enumerate(nums):
            carry_sum += num
            print("carrySum:",carry_sum)
            while carry_sum >= target:
                print("carrySum_while:",carry_sum)
                res = min(res, i - start + 1)
                carry_sum -= nums[start]
                start += 1
            print("carrySum_afet_while:",carry_sum)
        return res
nums = [2,3,1,2,4,3]
target = 7
result = Solution()
print(result.minSubArrayLen(nums, target))

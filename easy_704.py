from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            print(f"low:{low}",f"high: {high}")  # low and high gives list's index position
            mid = (low + high) //2
            guess = nums[mid]
            print(f"Guess: {guess}")  # guess is also the index position of the nums
            if guess == target:
                return mid
            
            elif guess > target:  
                high = mid - 1
                
            else:
                low = mid + 1
        return -1
nums = [-1,0,3,5,9,12]
target = 3    
sol = Solution()
res = sol.search(nums,target)           
print(res)
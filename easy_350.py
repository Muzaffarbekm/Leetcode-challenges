from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        
        p1 = p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 < num2:  
                p1 += 1
            elif num1 > num2:
                p2 += 1
            else:  # else responsible for catching matching 2 numbers and appends to the result
                result.append(num1)  
                p1 += 1
                p2 += 1
        print(result)
        return result
        
    
    
nums1 = [1,2,2,1]
nums2 = [2,2] 
sol = Solution()
res = sol.intersect(nums1,nums1)           
print(res)
''' Alice  swaps caandy X, she expects some specific quantity of candy Y back =>
=> Sum(A)-x+y = Sum(B)-y+x   =>  y = x+ Sum(A)-Sum(B)/2    answer [x,y]
'''

from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s = (sum(aliceSizes) - sum(bobSizes)) // 2  
        aliceSizes = set(aliceSizes)  
        
        for n in bobSizes:
            if s + n in aliceSizes:   # x= s+n  , y=n
                return [s + n, n]
            
aliceSizes = [2,2,3]
bobSizes = [2,2,1]
sol = Solution()
res = sol.fairCandySwap(aliceSizes,bobSizes)
print(res)
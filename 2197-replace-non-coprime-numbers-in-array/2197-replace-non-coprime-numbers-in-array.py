import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            stack.append(nums[i])
            while len(stack) >= 2 and math.gcd(stack[-1], stack[-2]) > 1:
                first = stack.pop()
                second = stack.pop()
                stack.append(math.lcm(first, second))
        return stack
            
            
                
                
            
            
        
        
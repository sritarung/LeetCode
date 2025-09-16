
class Solution:
    def gcd(self, n1, n2):
        a = n1
        b = n2
        while b:
            a, b = b, a % b
        return a
    def lcm(self, n1, n2):
        a = n1
        b = n2
        return abs(a * b)/self.gcd(n1,n2)
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            stack.append(nums[i])
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                first = stack.pop()
                second = stack.pop()
                stack.append(lcm(first, second))
        return stack
        
    nums = [6,4,3,2,7,6,2]

            
            
                
                
            
            
        
        
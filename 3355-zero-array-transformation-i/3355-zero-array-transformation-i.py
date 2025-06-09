class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # inputs: list of numbers >= 0, list of [l,r]
        # for each query list of l,r remove 1 from them
        # output: return true if numbers are 0 at the end of queries
        output = [0] * (len(nums) + 1)
        for l, r in queries:
            output[l] += 1
            output[r+1] -= 1
        operationCounts = []
        ops = 0
        for o in output:
            ops += o
            operationCounts.append(ops)
        
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True

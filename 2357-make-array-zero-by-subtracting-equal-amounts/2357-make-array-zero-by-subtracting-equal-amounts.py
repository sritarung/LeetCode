class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            if n != 0:
                numSet.add(n)
        return len(numSet)
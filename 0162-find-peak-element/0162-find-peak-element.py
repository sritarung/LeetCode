class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        # Loop continues as long as the search space has more than one element.
        while l < r:
            mid = l + (r - l) // 2
            
            # If the element to the right of mid is greater, we are on an "uphill" slope.
            # A peak must exist to the right, so we discard the left half.
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            # Otherwise, mid is on a "downhill" slope or is itself a peak.
            # A peak must exist in the left half (including mid).
            else:
                r = mid
        
        # The loop terminates when l == r, which is the index of a peak element.
        return l
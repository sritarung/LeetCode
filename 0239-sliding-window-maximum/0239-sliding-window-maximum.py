class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        d = deque()
        result = []
        for i in range(k):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
        result.append(nums[d[0]])
        for r in range(k, len(nums)):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if d[0] <= r - k:
                d.popleft()
            result.append(nums[d[0]])
    
        return result



[3,]
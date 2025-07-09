class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        memo = {}
        events.sort()
        def findNext(currentIndex):
            low = currentIndex + 1
            high = len(events)
            target = events[currentIndex][1]

            while low < high:
                mid = (low + high) // 2
                if events[mid][0] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low
        def dfs(i, remaining):
            if i == len(events) or remaining == 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            # skip current event
            skip = dfs(i + 1, remaining)
            
            # take current event
            j = findNext(i)  # binary search for next non-overlapping event
            take = events[i][2] + dfs(j, remaining - 1)
            
            memo[(i, remaining)] = max(take, skip)
            return memo[(i, remaining)]
        return dfs(0,k)
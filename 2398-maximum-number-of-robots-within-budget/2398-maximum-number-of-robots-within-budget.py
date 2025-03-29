class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(runningCosts)
        left = 0
        max_deque = deque()
        max_robots = 0
        sum_runningCosts = 0
        for right in range(n):
            while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
                max_deque.pop()
            max_deque.append(right)
            
            sum_runningCosts += runningCosts[right]
            
            while max_deque and chargeTimes[max_deque[0]] + (right - left + 1) * sum_runningCosts > budget:
                sum_runningCosts -= runningCosts[left]
                
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1	
            max_robots = max(max_robots, right - left + 1)
        return max_robots

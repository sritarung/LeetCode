class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(0, len(heights)-1):
            if heights[i] >= heights[i+1]:
                continue
            diff = heights[i+1] - heights[i]
            heapq.heappush(heap, -diff)
            if diff <= bricks:
                bricks -= diff
            else:
                if ladders > 0: 
                    bricks += -heapq.heappop(heap)
                    bricks -= diff
                    ladders -= 1
                else:
                    return i 

        return len(heights) - 1
        

                    

                
            


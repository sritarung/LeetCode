class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # lenght of grid
        N = len(grid)
        # to keep track of visited nodes(squares)
        visited = set()
        # priority queue to get the next least time to go to bottom right square
        minH = [[grid[0][0], 0, 0]]
        # the other directionally adj squares to go 
        directions= [[0,1], [1,0], [0, -1], [-1, 0]]

        visited.add((0,0))# add source to visited

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c==N-1:
                return t
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc

                if (newr < 0 or newc < 0 or newr==N or newc == N or (newr, newc) in visited):
                    continue
                visited.add((newr, newc))
                heapq.heappush(minH, [max(t, grid[newr][newc]), newr, newc])




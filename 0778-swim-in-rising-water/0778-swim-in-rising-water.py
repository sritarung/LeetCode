class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        visited.add((0,0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == M-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr,nc) in visited or nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                visited.add((nr,nc))
                heapq.heappush(minHeap, (max(t,grid[nr][nc]), nr, nc))

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m = len(heightMap)
        n = len(heightMap[0])

        visited = [[False]* n for _ in range(m)]
        heap = []

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m -1 or j == n -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        res = 0
        maxHeight = 0
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        while heap:
            height, x, y = heapq.heappop(heap)
            maxHeight = max(height, maxHeight)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    res += max(0, maxHeight - heightMap[nx][ny])
                    visited[nx][ny] = True
                    heapq.heappush(heap, (max(heightMap[x][y], heightMap[nx][ny]),nx, ny))
        return res



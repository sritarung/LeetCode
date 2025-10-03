class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        row = len(heightMap)
        col = len(heightMap[0])

        minHeap = []
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        res = 0
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        maxHeight = 0
        while minHeap:
            height, x, y = heapq.heappop(minHeap)
            maxHeight = max(maxHeight, height)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < row and 0 <= ny < col and heightMap[nx][ny] != -1:
                    res +=  max(0,maxHeight - heightMap[nx][ny])
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))
                    heightMap[nx][ny] = -1
        return res

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = [[False]*COLS for _ in range(ROWS)]
        atlantic = [[False]*COLS for _ in range(ROWS)]

        def dfs(i, j, visited, prevHeight):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or visited[i][j] or prevHeight > heights[i][j]:
                return
            visited[i][j] = True
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
        
        for r in range(ROWS):
            dfs(r,0, pacific,heights[r][0])
            dfs(r,COLS-1, atlantic,heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0,c, pacific,heights[0][c])
            dfs(ROWS-1,c, atlantic,heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
        
        return res





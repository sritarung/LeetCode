class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def backtrack(i, j):
            if i == len(triangle)-1:
                return triangle[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]

            down = backtrack(i+1, j)
            diag = backtrack(i+1, j+1)
            memo[(i,j)] = min(down, diag) + triangle[i][j]
            return memo[(i,j)]
        return backtrack(0,0)

    
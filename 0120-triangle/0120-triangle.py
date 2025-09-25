class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # two choices
        # move to i or i + 1 index
        self.answer = float('inf')
        memo = {}

        def backtrack(i, j, ans):
            if i == len(triangle):
                self.answer = min(self.answer, ans)
                return

            # prune if we already reached (i,j) with a better sum
            if (i, j) in memo and ans >= memo[(i, j)]:
                return
            memo[(i, j)] = ans

            backtrack(i+1, j, ans + triangle[i][j])
            backtrack(i+1, j+1, ans + triangle[i][j])

        backtrack(0, 0, 0)
        return self.answer
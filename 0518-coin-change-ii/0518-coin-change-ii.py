class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}  # Memoization dictionary

        def dfs(i, a):
            # Base case: amount is made up
            if a == 0:
                return 1
            # Base case: no more coins to consider
            if i >= len(coins):
                return 0
            # Return memoized result if available
            if (i, a) in memo:
                return memo[(i, a)]
            
            res = 0
            # If the current coin can be used
            if a >= coins[i]:
                # Use the current coin
                res += dfs(i, a - coins[i])
            # Skip the current coin and move to the next coin
            res += dfs(i + 1, a)
            
            # Memoize the result
            memo[(i, a)] = res
            return res

        # Start recursion with the first coin and the full amount
        return dfs(0, amount)
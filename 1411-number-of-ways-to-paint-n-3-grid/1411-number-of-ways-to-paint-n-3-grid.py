class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base Case for N=1
        # 6 ways to do ABC (3 colors)
        # 6 ways to do ABA (2 colors)
        abc = 6
        aba = 6
        
        for i in range(2, n + 1):
            # Calculate new values based on the formula
            new_abc = (2 * abc + 2 * aba) % MOD
            new_aba = (2 * abc + 3 * aba) % MOD
            
            # Update states
            abc = new_abc
            aba = new_aba
            
        return (abc + aba) % MOD
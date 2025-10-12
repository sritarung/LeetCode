class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        vals = sorted(freq.keys())
        n = len(vals)
        score = [v * freq[v] for v in vals]

        # 2) For each i, find the next index j with vals[j] >= vals[i] + 3
        #    (since choosing vals[i] forbids i±1 and i±2)
        next_idx = [n] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and vals[j] < vals[i] + 3:
                j += 1
            next_idx[i] = j

        # 3) DP from the back: dp[i] = max total starting at i
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            take = score[i] + dp[next_idx[i]]
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0] 
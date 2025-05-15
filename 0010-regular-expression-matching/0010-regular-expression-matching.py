class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(p):
                result = i == len(s)
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j+1] == '*':
                    result = (first_match and dp(i+1, j)) or dp(i, j+2)
                else:
                    result = (first_match and dp(i+1, j+1))
            memo[(i,j)] = result
            return result
        return dp(0,0)



# first condition: . matches char
# second condition: * matches previous char
# third condition: .* matches any chars




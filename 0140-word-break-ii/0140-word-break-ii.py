class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        result = []
        def backtrack(index, path):
            if index == len(s):
                result.append(" ".join(path))
                return
            for i in range(index, len(s)):
                if s[index: i+1] in wordSet:
                    path.append(s[index: i+1])
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0,[])
        return result

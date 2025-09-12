class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        def backtrack(index, sentence):
            if index == len(s):
                output.append(" ".join(sentence[:]))
                return
            for i in range(index, len(s)):
                if s[index: i +1] in wordDict:
                    sentence.append(s[index:i+1])
                    backtrack(i+1, sentence)
                    sentence.pop()
        backtrack(0, [])
        return output


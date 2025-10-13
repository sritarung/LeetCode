class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans =[words[0]]
        for i in range(1, len(words)):
            currWord = "".join(sorted(words[i]))
            prevWord = "".join(sorted(words[i-1]))
            if currWord == prevWord:
                continue
            else:
                ans.append(words[i])
        return ans



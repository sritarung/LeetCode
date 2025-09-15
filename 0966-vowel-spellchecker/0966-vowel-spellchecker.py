class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            ans = []
            for c in word:
                if c in 'aeiou':
                    ans += "*"
                else:
                    ans += c
            return "".join(ans)
        
        cap = {}
        vowel = {}
        normal = set(wordlist)
        for w in wordlist:
            word_low = w.lower()
            cap.setdefault(word_low, w)
            vowel.setdefault(devowel(word_low), w)


        output = []
        for q in queries:
            if q in normal:
                output.append(q)
                continue
            
            qLow = q.lower()
            if qLow in cap:
                output.append(cap[qLow])
                continue

            qVowel = devowel(qLow)
            if qVowel in vowel:
                output.append(vowel[qVowel])
                continue
            output.append("")
            
        return output

            



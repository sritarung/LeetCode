class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # this is like permutation in string, but return minimum string not true or false
        # need to return the minimum window substring of s that contains all the characters in string t. if no, return ""
        # input contains upper and lowercase english chars(52)
        # both the strings are of at least length one another edge case
        # if of same length, check counter of each char in both match or else return "" - same logic
        counter_t = Counter(t)
        need = len(counter_t)
        have = 0
        counter_s = defaultdict(int)
        left = 0
        idx = 0
        ans = float('inf')
        for right in range(len(s)):
            char = s[right]
            if char in counter_t:
                counter_s[char] += 1
                if counter_s[char] == counter_t[char]:
                    have += 1
                
            while have == need and left <=right:
                if right - left + 1 < ans:
                    ans = right - left + 1
                    idx = left
                left_char = s[left]
                counter_s[left_char] -= 1
                if left_char in counter_t:
                    if counter_s[left_char] == counter_t[left_char] - 1:
                        have -= 1
                left += 1
        return "" if ans == float('inf') else s[idx: idx + ans]


        

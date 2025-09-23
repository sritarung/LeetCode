class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        last_seen_s, last_seen_t = [0]*256, [0]*256
        for idx, (char_s, char_t) in enumerate(zip(s,t),1):
            ord_s = ord(char_s)
            ord_t = ord(char_t)

            if last_seen_s[ord_s] != last_seen_t[ord_t]:
                return False
            
            last_seen_s[ord_s] = last_seen_t[ord_t] = idx

        return True

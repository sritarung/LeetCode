class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        if len(s1) > len(s2):
            return False
        counter_s1 = Counter(s1)
        left = 0
        counter_s2 = defaultdict(int)
        required = len(counter_s1.keys())
        achieved = 0
        for right in range(len(s2)):
            char = s2[right]
            if char in counter_s1:
                counter_s2[char] += 1
                if counter_s1[char] == counter_s2[char]:
                    achieved += 1
                elif counter_s1[char] + 1 == counter_s2[char]:
                    achieved -= 1
                
            if right - left + 1 > len(s1):
                left_char = s2[left]
                if left_char in counter_s1:
                    if counter_s1[left_char] == counter_s2[left_char]:
                        achieved -= 1
                    elif counter_s1[left_char] == counter_s2[left_char]+1:
                        achieved += 1
                    counter_s2[left_char] -= 1
                left += 1
            
            if achieved == required and right - left + 1 == len(s1):
                return True
        return False
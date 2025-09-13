class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_mp = defaultdict(int)
        for i in range(len(arr)):
            element = arr[i]
            if element in freq_mp:
                freq_mp[element] += 1
            else:
                freq_mp[element] = 1

        freq_vals = sorted(freq_mp.values())
        unique_vals = len(freq_vals)
        removed = 0
        for freq in freq_vals:
            if freq + removed <= k:
                removed += freq
                unique_vals -= 1
            else:
                break
        return unique_vals 
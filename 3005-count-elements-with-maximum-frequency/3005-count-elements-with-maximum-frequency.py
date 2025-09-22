class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_map = {}
        max_frequency = 0
        max_frequency_total = 0

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1

            if frequency_map[n] > max_frequency:
                max_frequency = frequency_map[n]
                max_frequency_total = frequency_map[n]
            elif frequency_map[n] == max_frequency:
                max_frequency_total += frequency_map[n]
        
        return max_frequency_total
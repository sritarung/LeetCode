class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxEnergy = float('-inf')
        for i, e in enumerate(energy):
            total = 0
            pos = i
            while pos < len(energy):
                total += energy[pos]
                pos += k
            maxEnergy= max(maxEnergy, total)
        return maxEnergy

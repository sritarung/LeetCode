class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = [(spell, i) for i, spell in enumerate(spells)]
        sortedSpells.sort()
        potions.sort()
        ans = [0] * len(spells)
        j = len(potions)-1
        for spell, i in sortedSpells:
            while j >= 0 and spell * potions[j] >= success:
                j -= 1
            ans[i] = len(potions) - (j + 1)
        return ans
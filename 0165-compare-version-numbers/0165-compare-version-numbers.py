class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(max(len(v1), len(v2))):
            i1 = int(v1[i]) if i < len(v1) else 0
            i2 = int(v2[i]) if i < len(v2) else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        return 0

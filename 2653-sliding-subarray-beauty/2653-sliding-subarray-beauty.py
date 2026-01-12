class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        counter = [0] * 50
        ans = []

        for right in range(len(nums)):
            curr = nums[right]
            if curr < 0:
                counter[50+curr] += 1
            if right - left + 1 == k:
                count = 0
                for j in range(50):
                    count += counter[j]
                    if count >= x:
                        ans.append(j-50)
                        break   
                else:
                    ans.append(0) 
                if nums[left] <0:
                    counter[nums[left]+50] -= 1
                left += 1
        return ans


                
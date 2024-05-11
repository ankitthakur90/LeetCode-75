from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        maxi = 0.0
        sum = float(0.0)
        while j < len(nums):
            if j < k:
                sum += nums[j]
                if j == k - 1:
                    maxi = sum
                j += 1
            else:
                sum += nums[j] - nums[i]
                maxi = max(sum, maxi)
                j += 1
                i += 1
        return maxi / k
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = []
        rightSum= []
        sum = 0
        for i in nums:
            leftSum.append(sum)
            sum+=i
        sum  = 0
        for i in range(len(nums)-1,-1,-1):
            rightSum.append(sum)
            sum+=nums[i]
        rightSum.reverse()
        for i in range(len(nums)):
            if(leftSum[i] == rightSum[i]):
                return i
        return -1
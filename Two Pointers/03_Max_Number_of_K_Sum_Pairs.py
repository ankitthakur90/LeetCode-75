class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        right = len(nums)-1
        left = 0
        cnt = 0
        while(left< right):
            sum =nums[left] + nums[right]
            if( sum == k):
                cnt+=1
                left+=1
                right-=1
            elif(sum > k):
                right-=1
            else:
                left+=1
        return cnt
    

s1  =Solution()
nums = [1,2,3,4]
k = 5
print(s1.maxOperations(nums,k))
nums = [3,1,3,4,3]
k = 6
print(s1.maxOperations(nums,k))
nums = [1,2,1,5]
k = 3
print(s1.maxOperations(nums,k))
nums= [1,2,3,3,5,6]
k = 7
print(s1.maxOperations(nums,k))


## Brute force 

class Solution(object):
    def productExceptSelf(self, nums):
        if(nums.count(0) > 1):
            return [0] * len(nums)
        leftSum = [] 
        rightSum = []
        left = 0
        right = len(nums)-1
        while(left < len(nums)):
            k = left - 1
            if(left == 0):
                leftSum.append(1)
            else:
                prd = leftSum[k] * nums[k]
                leftSum.append(prd)
            left+=1
        k = 0
        while(right >=0):
            if(right == len(nums)-1):
                rightSum.append(1)
            else:
                prd = rightSum[k] * nums[right+1]
                rightSum.append(prd)
                k+=1
            right-=1
        rightSum.reverse()

        ind = 0
        while(ind < len(nums)):
            nums[ind] = leftSum[ind] * rightSum[ind]
            ind+=1
        return nums




# nums = [-1,1,0,-3,3]
# s1 = Solution()
# print(s1.productExceptSelf(nums))
# nums = [1,2,3,4]
# print(s1.productExceptSelf(nums))

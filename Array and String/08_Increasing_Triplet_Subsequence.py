class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        num1 = num2 = sys.maxsize
        for i  in nums:
            if(i <= num1):
                num1 = i
            elif(i <= num2):
                num2 = i
            else:
                return True
        return False
    
'''
s1 = Solution()
nums = [1,5,0,4,1,3]
print(s1.increasingTriplet(nums))
nums = [20,100,10,12,5,13]
print(s1.increasingTriplet(nums))
nums = [0,4,2,1,0,-1,-3]
print(s1.increasingTriplet(nums))
nums = [0,1,-2,2]
print(s1.increasingTriplet(nums))
nums = [20,100,10,12,5,13]
print(s1.increasingTriplet(nums))
nums = [5,1,5,5,2,5,4]
print(s1.increasingTriplet(nums))

'''
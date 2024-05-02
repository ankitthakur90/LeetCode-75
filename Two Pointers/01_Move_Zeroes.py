class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        if(cnt == -1):
            return 
        i = cnt
        ind = 0
        while(i != 0):
            if(nums[ind] == 0):
                nums.pop(ind)
                i-=1
            else:
                ind+=1
        while(cnt!=0):
            nums.append(0)
            cnt-=1 


#### Approach ---> 2  Optimal Solution


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        SizeOfZeros = 0
        i = 0
        while(i < len(nums)):
            if(nums[i] != 0):
                nums[i - SizeOfZeros],nums[i] = nums[i],nums[i-SizeOfZeros]
            else:
                SizeOfZeros+=1
            i+=1



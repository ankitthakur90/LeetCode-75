class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        mex = 0
        while(left <= right ):
            lVal = height[left]
            rVal = height[right]
            el = right - left
            sum = 1
            if(lVal < rVal):
                sum = lVal * el
                left+=1
            elif(lVal > rVal):
                sum = rVal * el
                right-=1
            else:
                sum = rVal* el
                left+=1
                right-=1
            if(sum >= mex):
                mex = sum
        # return mex
        print(mex)
    
s1  = Solution()
height = [1,8,6,2,5,4,8,3,7]
s1.maxArea(height)
height = [2,3,4,5,18,17,6]
s1.maxArea(height)
height = [2,5,8,6,4,9,3,1,5,4]
s1.maxArea(height)
height = [7,2,1,5,6,4,9,1,5]
s1.maxArea(height)
height = [1,2,5,8,7,6,4,13,9,4,23,1]
s1.maxArea(height)
height = [1,2,1]
s1.maxArea(height)
height = [1,2,4,3]
s1.maxArea(height)
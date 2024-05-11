class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        mexi = 0
        li = []
        sum = 0
        prv = 0
        for i in range(len(gain)):
            sum+=gain[i]
            if(sum > mexi):
                mexi  =sum
        return mexi
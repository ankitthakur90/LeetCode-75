class Solution(object):

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxi = 0
        sum = 0
        li = ['a', 'e', 'i', 'o', 'u']
        i = 0 
        j = 0
        sum = 0
        while(j< len(s)):
            if(j < k):
                if s[j] in li:
                    sum+=1
                    if(sum > maxi ):
                        maxi  = sum
                j+=1
            else:
                if s[i] in li:
                    if( sum > 0):
                        sum-=1
                if(s[j] in li):
                    sum+=1

                if(sum > maxi ):
                    maxi  = sum
                i+=1
                j+=1
        return maxi
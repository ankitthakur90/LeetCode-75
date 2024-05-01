class Solution(object):
    def reverseWords(self, s):
        tempLst = s.strip().split(" ")
        resLst = []
        for i in tempLst:
            if(i != ""):
                resLst.append(i)
        resLst.reverse()
        s = ' '.join(resLst)
        print(s)

s = "  a good   example  " 
s1 = Solution()
s1.reverseWords(s)
s = "the sky is blue"
s1.reverseWords(s)

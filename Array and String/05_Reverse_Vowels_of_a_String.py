from re import L


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        Approach - 1

        '''

        '''
        lst = []
        for  i  in range(len(s)):
            ch = s[i]
            if(ch == 'a' or ch == 'e' or ch == 'i'  or ch == 'o' or ch == 'u'):
                lst.append(ch)
            elif(ch == 'A' or ch == 'E' or ch== 'I' or ch == 'O' or ch == 'U'):
                lst.append(ch)

        lst.reverse()
        res = ""
        ind = 0
        for  i  in range(len(s)):
            ch = s[i]
            if(ch == 'a' or ch == 'e' or ch == 'i'  or ch == 'o' or ch == 'u'):
                vew = lst[ind]
                res +=vew
                ind+=1
            elif(ch == 'A' or ch == 'E' or ch== 'I' or ch == 'O' or ch == 'U'):
                vew = lst[ind]
                res +=vew
                ind+=1
            else:
                res+=ch
        return res
        '''

        '''
        Approach ===>>> 2 ( Using Two pointer)

        '''
        
        vowels = list("aeiouAEIOU")
        lst = list(s)
        left = 0
        right = len(lst)-1

        while left < right:
            while left < right and (lst[left] not in vowels):
                left+=1
            while left < right and (lst[right] not in vowels):
                right-=1
            lst[left],lst[right] = lst[right],lst[left]
            left+=1
            right-=1

        return ''.join(lst)

s = "leetcode"
s1 = Solution()
print(s1.reverseVowels(s))
    
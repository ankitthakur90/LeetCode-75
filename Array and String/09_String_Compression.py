class Solution(object):
    def returnCount(self, chars,ch,ind ):
        currCh = ch 
        cnt = 0
        while(currCh == ch and ind < len(chars) ):
            currCh = chars[ind]
            if(currCh == ch):
                cnt+=1
            else:
                return cnt
            ind+=1
        return cnt

    def compress(self, chars):
        if(len(chars)  <= 1):
            return len(chars)
        currCh = chars[0]
        prvCh = " "
        chars.append(" ")
        i = 0
        while( currCh != " "):
            currCh = chars[i]
            if(currCh == " "):
                break
            cnt = self.returnCount(chars,currCh,i)
            chars.append(currCh)
            if(cnt >=10):
                num = cnt
                cntLarge = []
                while(num != 0):
                    rem = num%10
                    cntLarge.append(rem)
                    num //=10
                ind = 0
                cntLarge.reverse()
                while(ind < len(cntLarge)):
                    cntCh = str(cntLarge[ind])
                    chars.append(cntCh)
                    ind+=1
            else:
                if(cnt != 1):
                    cntCh = str(cnt)
                    chars.append(cntCh)
            i = i + cnt
        currCh = chars[0]
        while(currCh != " "):
            currCh = chars[0]
            if(currCh == " "):
                break
            else:
                chars.pop(0)
        chars.pop(0)
        print(chars)


            
             






s1 = Solution()
lst = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s1.compress(lst)
lst = ["a","a","b","b","c","c","c"]
s1.compress(lst)

lst = ["a","b","b","b","b","b","b","b","b","b","b","a","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","a","b","b","c","c","c","a","b","@","@","2" ,"2","/","~","?","?","?","z","a","b","b","b","b","b","b","b","b","b","b","a","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","a","b","b","c","c","c","a","b","@","@","2" ,"2","/","~","?","?","?","z","a","b","b","b","b","b","b","b","b","b","b","a","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","a","b","b","c","c","c","a","b","@","@","2" ,"2","/","~","?","?","?","z","a","b","b","b","b","b","b","b","b","b","b","a","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","a","a","b","b","c","c","c","a","b","@","@","2" ,"2","/","~","?","?","?","z"]
s1.compress(lst)
lst = ["a" , "b","@","@","2" ,"2","/","~","?","?","?","z"]
s1.compress(lst)



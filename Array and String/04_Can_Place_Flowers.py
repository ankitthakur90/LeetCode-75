class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        #======>>>   Approach == 1 ========
        # if(n==0):
        #     return True
        # if(len(flowerbed) <= 1 ):
        #     if(flowerbed[0] !=1 and n ==1):
        #         return True
        #     return False
        # if(flowerbed[0] == 0 and flowerbed[1] == 0 ):
        #     n-=1
        #     flowerbed[0] = 1
        # for i in range(1,len(flowerbed)-1):
        #     if(flowerbed[i-1] !=1 and flowerbed[i+1] !=1 and flowerbed[i] !=1):
        #         n-=1
        #         flowerbed[i] = 1
        #         i+=1
        #     if(n == 0):
        #         return True
        # sz = len(flowerbed)-2
        # if(flowerbed[sz] !=1 and flowerbed[sz+1] !=1 ):
        #     n-=1
        # if(n <= 0):
        #     return True
        # return False

        # 2nd apporach

        i = 0 
        cnt = 0
        while(i < len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                cnt+=1
            i+=1
        return cnt >= n
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)

        res = []
        ind= 0
        while(ind < len(candies)):
            if(candies[ind]+extraCandies >= maxi):
                flg = True
                res.append(flg)
            else:
                flg = False
                res.append(flg)
            ind+=1
        return res


candies = [4,2,1,1,2]
extraCandies = 1
s1 = Solution()
print(s1.kidsWithCandies(candies,extraCandies))
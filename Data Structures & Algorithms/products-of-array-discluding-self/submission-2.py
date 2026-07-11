class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = []
        suffixProd = []
        prefixProd.append(nums[0])
        for i in range(1,len(nums)):
            prefixProd.append(nums[i]*prefixProd[i-1])

        suffixProd.append(nums[-1])
        for i in range(1, len(nums)):
            suffixProd.append(suffixProd[i-1]*nums[-1-i])
        suffixProd.reverse()

        #1, 2, 3, 4, 6
        #i =    1  2  3
        #iters: 6, 24, 144
        
        print(suffixProd, prefixProd)

        res = []
        res.append(suffixProd[1])
        for i in range(1, len(nums)-1):
            res.append(prefixProd[i-1]*suffixProd[i+1])
        res.append(prefixProd[-2])
        return res



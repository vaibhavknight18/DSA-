class Solution:
    def maxSubArray(self,nums):
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxProd,minProd = minProd,maxProd
            maxProd = max(nums[i],nums[i]*maxProd)
            minProd = min(nums[i],nums[i]*minProd)
            res=max(res,maxProd)
        print(res)
if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    s = Solution()
    s.maxSubArray(nums)

#brute force O(n2)
class Solution:
    def maxSubArray(self,nums):
        maxSum = float('-inf')
        for i in range(len(nums)):
            currSum = 0
            for j in range(i,len(nums)):
                currSum = currSum + nums[j]
                maxSum = max(maxSum , currSum)
        print(maxSum)
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    s.maxSubArray(nums)

#Optimised 
class Solution:
    def maxSubArray(self,nums):
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            currSum += num
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        print(maxSum)
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    s.maxSubArray(nums)

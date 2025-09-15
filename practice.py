#leetcode answers 

#1.TwoSum (optimised o(n)):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        while i < len(nums):
            needed = target - nums[i]
            if needed in hashmap:
                return [hashmap[needed],i]
            hashmap[nums[i]] = i
            i+=1
#2.SumArraySum equals k:
from collections import defaultdict
class Solution:
    def subArraySum(self,nums,k):
        prefix_sum = defaultdict(int)
        count = 0
        currSum = 0
        prefix_sum[0] = 1
        for num in nums:
            currSum = currSum + num
            if (currSum - k) in prefix_sum:
                count += prefix_sum[currSum - k]
            prefix_sum[currSum] += 1
        print(count)
if __name__ == "__main__":
    nums = [1,2,3]
    k=3
    s = Solution()
    s.subArraySum(nums,k)
#3. Search in rotated sorted array:
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or nums[l] > target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid-1
                else:
                    l = mid + 1
        return -1
    #4. Minimum in rotated sorted array:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l= mid+1
            else:
                r = mid
        return nums[l]
    


        
        

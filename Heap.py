#1.top k highest frequency elemnts: BRUTE FORCE 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_items = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for item in sorted_items[:k]:
            res.append(item[0])
        return res
      #OPTIMAL 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap =[]
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for count,num in heap:
            res.append(num)
        return res

#3.Kth largest elemnt in array: OPTIMAL
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        

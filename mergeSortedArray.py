#Brute Forec with extra space:
class Solution:
    def merge(self,nums1,m,nums2,n):
        temp = nums1[:m] + nums2
        temp.sort()
        for i in range(len(temp)):
            nums1[i] = temp[i]
        print(nums1)
if __name__ == "__main__":
    m = int(input("Enter req len of m:"))
    n = int(input("Enter req length of n:"))
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    s = Solution()
    s.merge(nums1,m,nums2,n)
  #Optimised 
  class Solution:
    def merge(self,nums1,m,nums2,n):
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        print(nums1)
if __name__ == "__main__":
    m = int(input("Enter req len of m:"))
    n = int(input("Enter req length of n:"))
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    s = Solution()
    s.merge(nums1,m,nums2,n)
    

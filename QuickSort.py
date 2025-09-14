class Solution:
    def quick_sort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr,low,high)
            self.quick_sort(arr,low,pi-1)
            self.quick_sort(arr,pi+1,high)
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low-1
        for j in range(low,high):
            if arr[j] <= pivot:
                i+=1
                arr[j],arr[i]=arr[i],arr[j]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
if __name__=="__main__":
    arr = [7,6,3,2,1]
    print("Original array:",arr)
    s = Solution()
    s.quick_sort(arr,0,len(arr)-1)
    print("Sorted array:",arr)

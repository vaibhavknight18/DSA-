class MergeSort:
    def merge_sort(self, nums):
        self.merge_sort_helper(nums, 0, len(nums) - 1)

    def merge_sort_helper(self, nums, first, last):
        if first < last:
            mid = (first + last) // 2
            self.merge_sort_helper(nums, first, mid)
            self.merge_sort_helper(nums, mid + 1, last)
            self.merge(nums, first, mid, last)

    def merge(self, nums, first, mid, last):
        # Left and Right subarrays
        L = nums[first:mid + 1]
        R = nums[mid + 1:last + 1]

        # Add sentinel values (very large numbers)
        L.append(999999999)
        R.append(999999999)

        i = j = 0
        for k in range(first, last + 1):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    n = int(input("Enter length:"))
    nums = list(map(int,input("Enter the list:").split()))
    print("Before sorting:",nums)
    sorter = MergeSort()
    sorter.merge_sort(nums)
    print("Ater Sorting:",nums)

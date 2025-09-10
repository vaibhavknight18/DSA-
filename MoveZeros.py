#Brute force extra space
class Solution:
    def moveZeros(self,A):
        zeros = []
        non_zeros = []
        for num in A:
            if num == 0:
                zeros.append(num)
            else:
                non_zeros.append(num)
        A[:] = non_zeros + zeros
        print(A)
if __name__ == "__main__":
    A = [1,0,3,0,4]
    ans = Solution()
    ans.moveZeros(A)
#optimkized
class Solution:
    def moveZeros(self,A):
        pos = 0 #pos=len(A)-1 #frontzeros
        for i in range(len(A)): #for i in range(len(a)-1,-1,-1): #frontzeros
            if A[i] != 0:
                A[pos] , A[i] = A[i] , A[pos]
                pos+=1
        print(A)a
if __name__ == "__main__":
    A = [1,0,3,0,4]
    ans = Solution()
    ans.moveZeros(A)

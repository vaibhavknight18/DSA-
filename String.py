#Reversing a string:
class Solution:
    def ReverseString(self,S):
        clean = ""
        for ch in  S:
            if ch.isalnum() or ch == " ":
                clean += ch.lower()
        print(clean[::-1])
if __name__=="__main__":
    S = input("Enter the name:")
    print(S)
    ans = Solution()
    ans.ReverseString(S)

  #2.len of longest substring without repeting chrecters :
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            seen = set()
            j = i
            while j < n and s[j] not in seen:
                seen.add(s[j])
                max_len = max(max_len,j-i+1)
                j += 1
        return max_len

        

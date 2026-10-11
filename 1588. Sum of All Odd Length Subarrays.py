class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans = sum(arr)
        n = len(arr)
        for i in range(n):
            for j in range(i+2,n,2):
                ans += sum(arr[i:j+1])
        return ans
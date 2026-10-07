class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        ans1 = 0
        if n < 3:
            return False
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                ans1 = i + 1
            else:
                break

        if ans1 == 0 or ans1 == n-1:
            return False

        for j in range(ans1,n-1):
            if arr[j] <= arr[j+1]:
                return False
        return True

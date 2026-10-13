class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        result = 0
        for  val in nums:
            ans.append(val*val)
        ans.sort()
        for i in range(n):
            if i >= n//2 :
                result += ans[i]
            else:
                result -= ans[i]
        return result         


        
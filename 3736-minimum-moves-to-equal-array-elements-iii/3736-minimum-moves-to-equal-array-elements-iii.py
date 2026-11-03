class Solution:
    def minMoves(self, nums: List[int]) -> int:
        counnt=0
        mx=max(nums)
        for val in nums:
          counnt=counnt+(mx-val)
        return counnt
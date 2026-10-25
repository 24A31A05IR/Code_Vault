class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if i-k < 0 or nums[i] > nums[i-k]:
                if  i+k >= len(nums) or nums[i] > nums[i+k]:
                    ans += nums[i]
        return ans        

        
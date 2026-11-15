class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        c = set(nums3)

        ans = []

        for num in a | b | c:
            if (num in a) + (num in b) + (num in c) >= 2:
                ans.append(num)

        return ans
        
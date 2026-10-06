class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums1)):
            indexx = nums2.index(nums1[i])
            for j in range(indexx,len(nums2)):
                if nums1[i] != nums2[j] and nums1[i] < nums2[j]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans
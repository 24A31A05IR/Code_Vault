class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ans = []

        for val in arr:

            if arr.count(val) == 1:
               ans.append(val)

        if k > len(ans):
            return ""
            
        return ans[k-1]        
        
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ans = []
        freq = Counter(arr)
        for val in arr:

            if freq[val] == 1:
               ans.append(val)

        if k > len(ans):
            return ""
            
        return ans[k-1]        
        
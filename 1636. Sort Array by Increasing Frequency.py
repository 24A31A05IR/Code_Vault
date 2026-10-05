class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)
        for val in nums:
            freq[val] += 1
        ans = []
        res = sorted(freq,key = lambda x:(freq[x],-x))
        for val in res:
            for i in range(freq[val]):
                ans.append(val)
        return ans
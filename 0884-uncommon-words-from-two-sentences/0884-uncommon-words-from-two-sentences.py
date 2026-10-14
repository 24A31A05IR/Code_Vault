class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        freq = defaultdict(int)
        ans = []
        newx = s1 +" " + s2
        for val in newx.split():
            freq[val] += 1
        for key,val in freq.items():
            if val == 1:
                ans.append(key)
        return ans        


        
        
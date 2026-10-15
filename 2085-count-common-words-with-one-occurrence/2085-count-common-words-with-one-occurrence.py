class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        ans = 0
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for val in words1:
            freq1[val] += 1

        for val in words2:
            freq2[val] += 1

        for key in freq1.keys():

            if freq1[key] == freq2[key] == 1:
                ans += 1

        return ans                     
        
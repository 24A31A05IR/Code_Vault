class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        freq = defaultdict(int)

        for val in deck:
            freq[val] += 1
            
        n= 0
        for val in freq.values():
             n = math.gcd(n,val)
        return n >= 2        
        
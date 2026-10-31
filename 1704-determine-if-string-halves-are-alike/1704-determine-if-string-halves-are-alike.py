class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ans = 0
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        vowels = "aeiouAEIOU"
        for val in a:
            if val in vowels:
                ans += 1
        for val in b:
            if val in vowels:
                ans -= 1
        return True if ans == 0 else False        

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        countt = 0
        ans = 0
        for val in s:
            if val == "(":
                countt += 1
            elif val == ")":
                if countt > 0:
                    countt -= 1
                else:
                    ans += 1
        return countt + ans
        
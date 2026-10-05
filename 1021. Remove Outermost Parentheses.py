class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c = 0 
        ans = ""
        for val in s:
            if val == '(':
                c += 1
                if c > 1:
                    ans += val
            else:
                c -= 1
                if c > 0:
                    ans += val
        return ans
        
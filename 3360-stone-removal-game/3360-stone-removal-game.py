class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        x = 10
        while n >= x:
            n -= x
            x -= 1
            ans = not ans
        
        return ans
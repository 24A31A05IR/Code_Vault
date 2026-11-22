class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if "ba" in s:
                return False
        return True        
        
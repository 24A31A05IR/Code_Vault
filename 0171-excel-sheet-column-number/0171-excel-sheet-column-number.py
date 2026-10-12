class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for val in columnTitle:
            ans = ans*26+(ord(val)-ord('A')+1)
        return ans    
        
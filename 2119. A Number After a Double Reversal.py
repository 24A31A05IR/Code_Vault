class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = str(num)[::-1]
        rev2 = str(int(rev1))[::-1]
        if int(rev2) == num:
            return True
        else:
            return False
        
        
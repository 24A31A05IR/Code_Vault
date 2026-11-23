class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1:
            if n in a:
                return False
            a.add(n)
            s=0
            while n>0:
                digit=n%10
                s+=digit*digit
                n=n//10
            n=s
        return True
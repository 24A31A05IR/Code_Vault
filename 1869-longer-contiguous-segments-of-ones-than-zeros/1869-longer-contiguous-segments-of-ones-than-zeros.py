class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeroes , ones = 0 , 0
        max1 ,max2 = 0 , 0

        for val in s:
            
            if val == "1":
                ones += 1
                max1 = max(max1,ones)
                zeroes = 0

            elif val == "0":
                zeroes +=1
                max2 = max(max2,zeroes)
                ones = 0

        return max1 > max2        
 
        
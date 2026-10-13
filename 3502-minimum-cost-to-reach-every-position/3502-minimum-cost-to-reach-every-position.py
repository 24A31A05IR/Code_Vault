class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        prefix = []

        minx = float('inf')

        for i in range(len(cost)):

            minx = min(minx,cost[i])

            prefix.append (minx)

        return prefix   
            
        
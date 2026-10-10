class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda row: row[1], reverse=True)
        for a, b in boxTypes:
            if a < truckSize:
                ans += a*b
                truckSize -= a
            else:
                ans += truckSize*b
                break
        return ans
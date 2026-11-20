class Solution:
    def maxWidthOfVerticalArea(self, points):
        x = []
        for i in points:
            x.append(i[0])
        x.sort()
        maximum = 0
        for i in range(1, len(x)):
            maximum = max(maximum, x[i] - x[i-1])
        return maximum
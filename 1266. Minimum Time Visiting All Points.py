class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        c = 0
        l = 0
        r = 1

        while r < len(points):
            x = abs(points[l][0] - points[r][0])
            y = abs(points[l][1] - points[r][1])

            c += max(x, y)

            l += 1
            r += 1

        return c
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range(len(grid)-2):
            row = []
            for j in range(len(grid)-2):
                maxi = 0

                for x in range(i, i+3):
                    for y in range(j, j+3):
                        maxi = max(maxi, grid[x][y])

                row.append(maxi)

            ans.append(row)

        return ans
class Solution:
    def reformatDate(self, date: str) -> str:
        ans = ""
        months = {
                    "Jan": 1,
                    "Feb": 2,
                    "Mar": 3,
                    "Apr": 4,
                    "May": 5,
                    "Jun": 6,
                    "Jul": 7,
                    "Aug": 8,
                    "Sep": 9,
                    "Oct": 10,
                    "Nov": 11,
                    "Dec": 12
                }
        date = date.split()
        for i in range(len(date)-1,-1,-1):
            if i  == 2:
                ans += date[i]
            elif i == 1:
                ans += "-" + str(months[date[i]]).zfill(2)
            else:
                ans += "-" + date[i][:-2].zfill(2)
        return ans
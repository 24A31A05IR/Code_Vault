class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        new = defaultdict(int)
        for i,val in enumerate(s):
            if val not in new:
                new[val] = i
            else:
                dist = i - new[val] - 1
                if dist != distance[ord(val)-97]:
                    return False
        return True
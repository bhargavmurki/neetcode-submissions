class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for s, e in intervals[1:]:
            lastend = res[-1][1]

            if s <= lastend:
                res[-1][1] = max(lastend, e)
            else:
                res.append([s, e])
        return res
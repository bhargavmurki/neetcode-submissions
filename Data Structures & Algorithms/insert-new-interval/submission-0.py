class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        l , r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if intervals[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        
        intervals.insert(l, newInterval)

        res = []
        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
            
        return res
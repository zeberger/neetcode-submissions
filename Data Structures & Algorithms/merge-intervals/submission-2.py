class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []
        currentMaxInterval = [intervals[0][0], intervals[0][1]]
        for list_i in intervals:
            if list_i[0] <= currentMaxInterval[1] and list_i[1] >= currentMaxInterval[1]:
                currentMaxInterval[1] = list_i[1]
            elif list_i[0] > currentMaxInterval[1]:
                res.append(currentMaxInterval)
                currentMaxInterval = [list_i[0], list_i[1]]

        res.append(currentMaxInterval)
        return res
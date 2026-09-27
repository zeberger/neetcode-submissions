class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        freq = dict(sorted(freq.items(), key = lambda item : item[1], reverse = True))
        for key in freq:
            if len(res) >= k:
                break
            else:
                res.append(key)
        
        return res

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        i = 0
        for num in nums:
            diff = target - num

            if diff in numsDict:
                return [numsDict[diff], i]
            
            numsDict[num] = i
            i += 1
        return []



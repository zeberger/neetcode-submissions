class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total = len(nums)
        fixed_nums = set(nums)
        new_total = len(fixed_nums)
        if total > new_total:
                return True
        return False



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) - 1
        res = [None] * (length + 1)
        upProd = [nums[0]] * (length + 1)
        downProd = [nums[-1]] * (length + 1)
        for i in range(length):
            if i == 0: continue
            upProd[i] = upProd[i -1] * nums[i]
            downProd[length - i] = downProd[length - i + 1] * nums[length - i]
        for j in range(length +1):
            if j == 0:
                res[j] = downProd[j + 1]
            elif j == length:
                res[j] = upProd[j - 1]
            else:
                res[j] = upProd[j - 1] * downProd[j + 1]
        return res
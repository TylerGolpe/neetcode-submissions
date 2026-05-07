class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        for i in range(len(nums)):
            temp = 1
            j = 0
            for j in range(len(nums)):
                if j != i:
                    temp *= nums[j]
            output.append(temp)
        return output



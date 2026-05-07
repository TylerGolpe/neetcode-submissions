class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in newDict:
                return [newDict[complement], i]
            newDict[nums[i]] = i
        
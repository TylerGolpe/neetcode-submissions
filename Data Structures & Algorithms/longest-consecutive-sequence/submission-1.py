class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        counter = 1
        if len(nums) == 0:
            return 0
        sortedNums = sorted(set(nums))
        current = sortedNums[0]
        for i in range(1, len(sortedNums)):
            print(i)
            if sortedNums[i] == current + 1:
                counter += 1
            else:
                output = max(counter, output)
                counter = 1
            current = sortedNums[i]
        output = max(counter, output)
        return output
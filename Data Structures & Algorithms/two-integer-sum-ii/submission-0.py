class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            hashMap[numbers[i]] = i + 1
        for num in numbers:
            complement = target - num
            if complement in hashMap and num < complement:
                return [hashMap[num], hashMap[complement]]
        return 0
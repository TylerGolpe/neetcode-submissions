class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            print(count)
        for num, cnt in count.items():
            freq[cnt].append(num)
            print(freq)

        output = []
        for i in range(len(freq) - 1, 0, -1):
            print(i)
            for num in freq[i]:
                print(num)
                output.append(num)
                if len(output) == k:
                    return output

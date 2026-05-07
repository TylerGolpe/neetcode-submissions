class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Set a value to the length of the list
        #Create 3 arrays, with sizes = the length of the list
        prefix = [0] * n
        suffix = [0] * n
        output = [0] * n

        #The prefix, at position 0, should be 1, as nothing exists to the left of the first index
        #Similarly, the suffix, at position n - 1, should be 1, since nothing 
        #is to the right of the last index
        prefix[0] = suffix[n - 1] = 1
        #For items in the range of 1 to the length, skipping 0 due to our setup line above
        for i in range(1, n):
            #We'll take the position at prefix[1], set it equal to nums[0] * prefix[0]
            #This will be the value of nums[0] * 1. This works since nothing would come before anyways.
            prefix[i] = nums[i - 1] * prefix[i - 1]
            #We move through the rest of the values the same way for the prefixes.
            #For each prefix, we're multiplying the previous value by the new number in order.
        for i in range(n - 2, -1, -1):
            #For the suffix, we're doing the same algorithm, but from the opposite end.
            #This means we're "accumulating" all the values from the end, to our pointer, EXCEPT the pointer
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            #Finally, we're taking the values of "everything prior" and "everything after"
            #And we set those to the output of that position
            output[i] = prefix[i] * suffix[i]
        return output

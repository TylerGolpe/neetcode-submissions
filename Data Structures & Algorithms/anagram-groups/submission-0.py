class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = {}
        for word in strs:
            current = "".join(sorted(word))
            if current in hashSet:
                hashSet[current] += [word]
            else:
                hashSet[current] = [word]
        return list(hashSet.values())
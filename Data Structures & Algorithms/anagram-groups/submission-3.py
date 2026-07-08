class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in anagrams:
                anagrams[sortedString].append(s)
            else:
                anagrams[sortedString] = [s]
        
        res = []
        for key in anagrams:
            res.append(anagrams[key])

        return res
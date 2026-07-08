class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            dummy = "".join(sorted(string))
            if dummy in anagrams:
                anagrams[dummy].append(string)
            else:
                anagrams[dummy] = [string]
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        
        return res
        
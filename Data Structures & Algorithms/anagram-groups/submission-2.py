class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sort = "".join(sorted(string))
            if sort in anagrams:
                anagrams[sort].append(string)
            else:
                anagrams[sort] = [string]
        
        result = []
        for values in anagrams.values():
            result.append(values)
        return result
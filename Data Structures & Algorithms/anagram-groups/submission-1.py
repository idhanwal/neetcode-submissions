class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in anagrams:
                arr = anagrams[sorted_str]
                arr.append(str)
                anagrams[sorted_str] = arr
            else:
                anagrams[sorted_str] = [str]
        
        res = []
        for key in anagrams:
            res.append(anagrams[key])

        return res
        
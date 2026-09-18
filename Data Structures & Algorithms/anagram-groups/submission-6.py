class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for s in strs:
            sortedString = "".join(sorted(s))
            anagrams[sortedString].append(s)
        
        return list(anagrams.values())
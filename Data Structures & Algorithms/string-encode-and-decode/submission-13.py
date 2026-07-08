class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "*" + strs[i]

        return "".join(strs) 
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            size = int(s[i : j])
            k = j + 1 + size
            res.append(s[j + 1 :  j + 1 + size])
            i = k
        
        return res

            

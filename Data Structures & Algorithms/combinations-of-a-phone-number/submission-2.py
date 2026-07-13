class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {2 : ['a', 'b', 'c'],
                    3: ['d', 'e', 'f'],
                    4: ['g', 'h', 'i'],
                    5: ['j', 'k', 'l'],
                    6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'],
                    8: ['t', 'u', 'v'],
                    9: ['w', 'x', 'y', 'z']}

        res = []
        def dfs(i, sub):
            if i >= len(digits):
                res.append(sub)
                return
            
            for ch in digitMap[int(digits[i])]:
                sub += ch
                dfs(i + 1, sub)
                sub = sub[:len(sub) - 1]
        dfs(0, "")
        return res

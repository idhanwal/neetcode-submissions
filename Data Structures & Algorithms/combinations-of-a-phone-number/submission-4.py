class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']
        }

        res = []

        def rec(i, comb):
            if i >= len(digits):
                res.append("".join(comb[::]))
                return
            
            for val in mapper[int(digits[i])]:
                comb.append(val)
                rec(i + 1, comb)
                comb.pop()
            
        rec(0, [])

        return res
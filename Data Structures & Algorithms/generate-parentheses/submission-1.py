class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def rec(open, close, comb):
            if open == n and close == n:
                res.append(comb[::])
                return
            
            if open < n:
                comb += "("
                rec(open + 1, close, comb)
                comb = comb[:-1]
            if close < open:
                comb += ")"
                rec(open, close + 1, comb)

        
        rec(0, 0, "")
        return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec(o,c):
            if o ==n and c == n:
                res.append("".join(stack))
                return
            
            if o < n:
                stack.append("(")
                rec(o + 1, c)
                stack.pop()
            if c < o:
                stack.append(")")
                rec(o, c + 1)
                stack.pop()
        
        rec(0, 0)
        return res


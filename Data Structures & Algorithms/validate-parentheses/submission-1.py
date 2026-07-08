class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"[": "]", "{" : "}", "(": ")"}
        for ch in s:
            if ch in ["[", "{", "("]:
                stack.append(ch)
            elif ch in ["]", "}", ")"]:
                if len(stack) > 0 and pair[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

        
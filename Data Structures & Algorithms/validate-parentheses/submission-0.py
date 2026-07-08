class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"[": "]", "{" : "}", "(": ")"}
        for ch in s:
            print("hello : " + str(stack))
            if ch in ["[", "{", "("]:
                stack.append(ch)
            elif ch in ["]", "}", ")"]:
                if len(stack) > 0 and pair[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        print("yello : " + str(stack))
        if len(stack) == 0:
            print("hello")
            return True
        return False

        
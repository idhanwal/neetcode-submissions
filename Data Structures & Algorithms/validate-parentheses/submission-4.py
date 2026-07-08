class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ")", "{":"}", "[":"]"}
        i = 0

        while i < len(s):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            else:
                # pop = stack.pop()
                if stack and s[i] == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
            i += 1
        if len(stack) != 0:
            return False
        return True
        
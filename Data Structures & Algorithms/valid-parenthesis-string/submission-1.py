class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        left = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return not left
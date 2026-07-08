class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window = {}
        target = {}
        for ch in t:
            target[ch] = 1 + target.get(ch, 0)

        need = len(target)
        have = 0
        l = 0
        res = ""
        res_len = float('inf')
        for r in range(len(s)):
            right = s[r]
            window[right] = 1 + window.get(right, 0)
            if right in target and window[right] == target[right]:
                have += 1
            
            while l <= r and have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1 
                    res = s[l:r + 1]
                    print(res)
                left = s[l]
                window[left] = window[left] - 1
                if left in target and target[left] > window[left]:
                    have -= 1
                l += 1
            
        return res


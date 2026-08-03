class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n + 1)

        for i in range(len(res)):
            count = 0
            num = i
            for j in range(32):
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            res[i] = count
        return res 
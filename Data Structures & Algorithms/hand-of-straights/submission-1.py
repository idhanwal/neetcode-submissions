class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        mapper = Counter(hand)
        # start = min(mapper.keys())
        # while mapper:
        #     for i in range(start, start + groupSize):
        #         if i not in mapper:
        #             print(i)
        #             return False
        #         mapper[i] -= 1
        #         if mapper[i] == 0:
        #             del mapper[i]
        #     if not mapper:
        #         return True
        #     start = min(mapper.keys())
        # return True
        
        for num in hand:
            start = num
            while mapper[start - 1]:
                start -= 1
            
            while start <= num:
                while mapper[start]:
                    for i in range(start, start+groupSize):
                        if not mapper[i]:
                            return False
                        mapper[i] -= 1
                start += 1
        return True
            
        
        

            
            
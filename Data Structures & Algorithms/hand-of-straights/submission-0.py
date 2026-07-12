class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        mapper = Counter(hand)
        start = min(mapper.keys())
        print(start)
        while mapper:
            for i in range(start, start + groupSize):
                if i not in mapper:
                    print(i)
                    return False
                print("useing ", i)
                mapper[i] -= 1
                if mapper[i] == 0:
                    del mapper[i]
            if not mapper:
                return True
            start = min(mapper.keys())
            print(start)
        return True
        
            
        
        

            
            
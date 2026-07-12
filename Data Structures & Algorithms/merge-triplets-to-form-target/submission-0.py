class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        for triplet in triplets:
            for a, b in zip(triplet, target):
                if a > b:
                    break
            else:
                valid.append(triplet)
        
        for i, val in enumerate(target):
            for j in range(len(valid)):
                if val == valid[j][i]:
                    break
            else:
                return False

        return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind_map = defaultdict(list)


        for i, num in enumerate(nums):
            ind_map[num].append(i)
        
        for key in ind_map:
            if len(ind_map[key]) > 1:
                dup = ind_map[key]

                l = 0
                r = len(dup) - 1
                while l < r:
                    if dup[r] - dup[l] > k:
                        l += 1
                    else:
                        return True

                

        return False


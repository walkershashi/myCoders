class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cntr = {}
        for i in nums:
            if i not in cntr:
                cntr[i] = 1
            else:
                cntr[i] += 1
        
        res = []
        for key, cnt in cntr.items():
            if cnt == 2:
                res.append(key)
        
        return sorted(res)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range (len(nums)):
            if nums[i] in index.keys():
                return(index[nums[i]],i)
            else:
                pair = target - nums[i]
                index[pair] = i
        return -1

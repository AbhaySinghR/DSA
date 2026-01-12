class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap={}
        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[target-nums[i]]=i
            else:
                return [hmap[nums[i]],i]
        
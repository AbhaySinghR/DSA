class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        min_dis = float('inf')
        hmap = {}

        for j, x in enumerate(nums):
            if x in hmap:
                i = hmap[x]
                min_dis = min(min_dis, j - i)

            rev = int(str(x)[::-1])
            hmap[rev] = j


        return -1 if min_dis == float('inf') else min_dis

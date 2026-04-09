class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:

        cube_map = defaultdict(set)
        
        max_a = int(n ** (1/3)) + 1
        
        for a in range(1, max_a + 1):
            a3 = a ** 3
            if a3 > n:
                break
            for b in range(a, max_a + 1):
                s = a3 + b ** 3
                if s > n:
                    break
                cube_map[s].add((a, b))
        
        res = [x for x, pairs in cube_map.items() if len(pairs) >= 2]
        return sorted(res)
        
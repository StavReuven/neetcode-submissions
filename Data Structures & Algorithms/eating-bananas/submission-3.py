class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        small = 1
        big = 1
        for pile in piles:
            big = max(big, pile)
        
        ans = big
        while small <= big:
            mid = small + (big - small)//2
            res = 0
            for pile in piles:
                res += math.ceil(pile/mid)
            
            if res <= h:
                ans = min(mid, ans)
                big = mid - 1

            else:
                small = mid + 1

        return ans

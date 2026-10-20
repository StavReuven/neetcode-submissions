class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        maxc = 0
        for s in seen:
            cntr = 0
            cur = s
            if cur - 1 in seen:
                continue
            

            while cur in seen:
                cntr += 1
                cur += 1
            
            maxc = max(maxc, cntr)
        return maxc
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        sufix = [0] * len(height)
        maxh = 0
        for i in range(len(height)):
            maxh = max(maxh, height[i])
            prefix[i] = maxh
        maxh = 0
        for i in reversed(range(len(height))):
            maxh = max(maxh, height[i])
            sufix[i] = maxh
        sum = 0
        for i in range(len(height)):
            sum += min(sufix[i], prefix[i]) - height[i]
        
        return sum
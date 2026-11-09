class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        left = [0] * len(heights)
        right = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        stack = []

        for i in reversed(range(len(heights))):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)
            stack.append(i)

        for i in range(len(heights)):
            area = max(heights[i] * (right[i] - left[i] - 1),area)

        return area
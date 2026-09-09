class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for r in range(n + 1):
            while stack and (r == n or heights[stack[-1]] >= heights[r]):
                height = heights[stack.pop()]

                if not stack:
                    width = r
                else:
                    width = r - stack[-1] - 1

                maxArea = max(maxArea, height * width)

            stack.append(r)

        return maxArea
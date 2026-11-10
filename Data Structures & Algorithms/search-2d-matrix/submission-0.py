class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left = 0
                right = len(matrix[0]) - 1

                while left <= right:
                    midl = left + (right - left) // 2
                    if matrix[mid][midl] == target:
                        return True
                    elif matrix[mid][midl] > target:
                        right = midl - 1
                    else:
                        left = midl + 1
                return False

            elif matrix[mid][-1] > target:
                bottom = mid - 1
            else:
                top = mid + 1

        return False
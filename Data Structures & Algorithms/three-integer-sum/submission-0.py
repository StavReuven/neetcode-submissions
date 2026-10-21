class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = self.twoSum(nums, -nums[i], i + 1)
            for pair in temp:
                res.append([pair[0], pair[1], nums[i]])

        return res

    
    def twoSum(self, numbers: List[int], target: int, start: int) -> List[int]:
        left = start
        right = len(numbers) - 1
        ans = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                ans.append([numbers[left], numbers[right]])
                right -= 1
                left += 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return ans
class Solution:
    def appearenceInOrderedArray(self, nums, target):
        left = self.getFirstIndex(nums, target, 0, len(nums) - 1)
        right = self.getLastIndex(nums, target, 0, len(nums) - 1)
        return right - left + 1


    def getFirstIndex(self, nums, target, left, right):
        mid = (left + right) >> 1
        while left + 1 < right:
            if target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return None

    def getLastIndex(self, nums, target, left, right):
        mid = (left + right) >> 1
        while left + 1 < right:
            if target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                left = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return None



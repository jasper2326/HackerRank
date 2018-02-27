class Solution:
    def findSum(self, nums, sum):
        if not nums or len(nums) <= 1:
            return None

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == sum:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] < sum:
                i += 1
            else:
                j -= 1

        return None



    def findConyinousSequence(self, target):
        left, right = 1, 2
        result = []
        while left * 2 + 1 <= target:
            if sum(range(left, right + 1)) == target:
                result.append(range(left, right + 1))
            elif sum(range(left, right + 1)) < target:
                right += 1
            else:
                left += 1
        return result



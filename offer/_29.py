class Solution:
    def moreThanHalfNum(self, nums):
        if not nums or len(nums) == 0:
            return None

        result = nums[0]
        count = 0
        for i in range(1, len(nums), 1):
            if count == 0:
                result = nums[i]
                count = 1
            elif nums[i] == result:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == result:
                count += 1

        if count > len(nums) / 2:
            return result
        else:
            return 'Error'
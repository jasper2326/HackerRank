class Solution:
    def maxSubArray(self, nums):
        if not nums or len(nums) == 0:
            return 0

        maxSum = nums[0]
        minSum = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - minSum > maxSum:
                maxSum = sum - minSum
            if sum < minSum:
                minSum = sum
        return maxSum


a = Solution()
print(a.maxSubArray([1,-2,3,10,-4,7,2,-5]))
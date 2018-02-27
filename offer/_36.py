class Solution:
    def reversePairs(self, nums):
        self.tmp = [0] * len(nums)
        return self.mergeSort(nums, 0, len(nums) - 1)


    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0

        m = (left + right) >> 1
        ans = self.mergeSort(nums, left, m) + self.mergeSort(nums, m + 1, right)
        i, j, k = left, m + 1, left
        while i <= m and j <= right:
            pass

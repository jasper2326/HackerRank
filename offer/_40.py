class Solution:
    def uniqueNumber(self, nums):
        temp = []
        for num in nums:
            if num not in temp:
                temp.append(num)
            else:
                temp.remove(num)
        return temp
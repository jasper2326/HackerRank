class Solution:
    def minNumber(self, nums):
        nums.sort(cmp=self.cmp)
        result = ''.join([str(element) for element in nums])
        i, length = 0, len(result)
        while i + 1 < length:
            if result[i] != '0':
                break
            i += 1
        return result[i : ]



    def cmp(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return -1
        elif str(a) + str(b) == str(b) + str(a):
            return 0
        else:
            return 1
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        count = 0
        for i in range(32):
            count += num & 1
            num = num >> 1
        return count
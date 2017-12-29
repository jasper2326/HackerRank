class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        while b != 0:
            carry = a ^ b
            b = (a & b) << 1
            a = carry
        return a 
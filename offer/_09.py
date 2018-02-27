class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a
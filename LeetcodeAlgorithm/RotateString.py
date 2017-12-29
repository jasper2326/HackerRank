class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if len(str) > 0:
            offset = offset % len(str)

        temp = (str + str)[len(str) - offset: 2 * len(str) - offset]

        for i in range(len(temp)):
            str[i] = temp[i]
''' Replace all the spaces in a string with %20'''

class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if string is None or length == 0:
            return length

        spaces = 0
        for c in string:
            if c == ' ':
                spaces += 1

        L = length + spaces * 2
        index = L - 1
        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1
        return L
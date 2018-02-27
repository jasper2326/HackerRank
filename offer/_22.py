class Solution:
    def is_reverse(self, list1, list2):
        if len(list1) > len(list2):
            return False

        stack = []
        index = 0
        for num in list1:
            stack.append(num)
            while index < len(list2) and stack[-1] == list2[index]:
                index += 1
                stack.pop()

        return len(stack) == 0
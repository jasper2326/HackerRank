class Solution:
    def reorderList(self, A):
        if A is None or len(A) <= 1:
            return A

        temp = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                temp.append(A.pop(i))
        return A.extend(temp)


    def reorderList_2(self, A):
        if A is None or len(A) <= 1:
            return A

        left, right = 0, len(A) - 1
        while left < right:
            while left < right and A[left] % 2 == 1:
                left += 1
            while left < right and A[right] % 2 == 0:
                right -= 1

            A[left], A[right] = A[right], A[left]
        return A
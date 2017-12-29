class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []

        while A and B:
            if A[0] < B[0]:
                C.append(A.pop(0))
            else:
                C.append(B.pop(0))

        if A:
            C += A
        if B:
            C += B
        return C
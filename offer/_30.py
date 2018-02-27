class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        if k == 0:
            return []
        if k > len(tinput):
            return []

        result = []
        currentMax = tinput[0]
        for num in tinput:
            if not result or len(result) < k:
                result.append(num)
                currentMax = max(result)
                continue
            if num < currentMax:
                result.remove(currentMax)
                result.append(num)
                currentMax = max(result)
        ans = sorted(result)
        return ans

    def __init__(self, tinput, k):
        self.tinput = tinput
        self.l = k


a = Solution([], 0)
print(a.GetLeastNumbers_Solution([], 0))
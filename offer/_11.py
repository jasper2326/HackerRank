class Solution:
    def powerNormal(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base

        if exponent < 0:
            flag = 1
            exponent = -exponent
        else:
            flag = 0

        result = 1
        temp = base
        while exponent != 0:
            if exponent & 1 == 1:
                result = result * temp
            temp = temp ** 2
            exponent = exponent >> 1

        if flag == 0:
            return result
        else:
            return 1 / result



    def powerNormalRecursive(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base

        result = self.powerNormalRecursive(base, exponent >> 1)
        result *= result
        if exponent & 1 == 1:
            result *= base
        return result
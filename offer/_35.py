class Solution:
    def firstNotRepeatingChar(self, string):
        if not string or len(string) == 0:
            return None

        myMap = {}
        for i in range(len(string)):
            if string[i] in myMap.keys():
                myMap[string[i]].append(i)
            else:
                myMap[string[i]] = [i]

        result = len(string) + 1
        for indexs in myMap.values():
            if len(indexs) == 1:
                result = min(result, indexs[0])
        return string[result]

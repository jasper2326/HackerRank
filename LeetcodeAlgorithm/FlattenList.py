class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]

        result = []
        for element in nestedList:
            result.extend(self.flatten(element))
        return result
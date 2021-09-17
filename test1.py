# path = []+[1,3]+[2,3]
# print([]+[1,3]+[2,3])
# print([2,3] in path)
# print([[1,2],[1,2,3]])

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for v in nums:
            for i in range(len(ans)):
                member = ans.pop(0)
                ans.append(member+[v])
                ans.append(member)
        return ans

s = Solution()
print(s.subsets([1,2,3]))


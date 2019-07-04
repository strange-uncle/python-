'''
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # l = list(enumerate(nums))
        # g = ([k1, k2] for k1, v1 in l for k2, v2 in l if k1 != k2 and v1 + v2 == target)
        # for i in g:
        #     ##return i
        #     print(i)
        d = dict()
        nums_len = len(nums)
        for i in range(nums_len):
            gap = target - nums[i]
            if gap in d:
                return [d[gap], i]
            d[nums[i]] = i
        return None



data = Solution()
print(data.twoSum([2, 7, 11, 15], 26))





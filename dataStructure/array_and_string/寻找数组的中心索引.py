class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = sum(nums)

        for index,item in enumerate(nums):
            right_sum -= item

            if left_sum == right_sum:
                return index

            left_sum += item
        return -1


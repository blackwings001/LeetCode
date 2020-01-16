class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums

        new_head = k % len(nums)

        return nums[new_head:] + nums[:new_head]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution().rotate(nums, k)
    print(res)

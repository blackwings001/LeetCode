class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""

        nums = self.merge_sort(nums)
        nums = [str(i) for i in nums]

        return "".join(nums)

    def merge_sort(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums

        mid = len(nums) > 1  # 右移1代替除2

        return self.merge(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))

    def merge(self, nums1, nums2):
        merge_num = []

        def a_large_equal_b(a, b):
            a, b = str(a), str(b)
            n, m = len(a), len(b)

            if n < m:
                a, b = b, a
                n, m = m, n
                reverse = True
            else:
                reverse = False

            for i in range(n):
                j = i if i < m else i - m
                if a[i] > b[j]:
                    return True if not reverse else False
                elif a[i] < b[j]:
                    return False if not reverse else True

            return True if not reverse else False

        while nums1 and nums2:
            ele1 = nums1[0]
            ele2 = nums2[0]

            if a_large_equal_b(ele1, ele2):
                merge_num.append(nums1.pop(0))
            else:
                merge_num.append(nums2.pop(0))

        merge_num.extend(nums1)
        merge_num.extend(nums2)

        return merge_num


if __name__ == '__main__':
    nums = [2, 25]
    res = Solution().largestNumber(nums)
    print(res)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:
            return 0

        largest_area = 0
        for i in range(len(heights)):
            cur_height = heights[i]
            cur_area = 0
            for j in range(i, -1, -1):
                if heights[j] >= cur_height:
                    cur_area += cur_height
                else:
                    break
            for k in range(i, len(heights)):
                if heights[k] >= cur_height:
                    cur_area += cur_height
                else:
                    break
            cur_area -= cur_height
            if cur_area > largest_area:
                largest_area = cur_area

        return largest_area

if __name__ == '__main__':
    heights = [2,1,5,6,3,2]
    res = Solution().largestRectangleArea(heights)
    print(res)

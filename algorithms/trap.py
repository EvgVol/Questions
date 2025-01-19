class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        return water_trapped


def test_trap():
    s = Solution()
    assert s.trap([0,0,0,0,0,1,0,0,0]) == 0
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2]) == 6
    assert s.trap([4,2,0,3,2,5]) == 9
    assert s.trap([4,0,0,0,5]) == 12


test_trap()
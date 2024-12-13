class Solution(object):
    def longest_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ...


def test_longest_subarray():
    s = Solution()
    assert s.longest_subarray([0,1,1,0,1,0,1]) == 3
    assert s.longest_subarray([1,1,0,1]) == 3
    assert s.longest_subarray([0,1,1,1,0,1,1,0,1]) == 5
    assert s.longest_subarray([1,1,1]) == 2

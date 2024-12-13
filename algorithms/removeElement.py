class Solution(object):
    def removeElement(self, nums: list, val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
        



def test_removeElement():
    s = Solution()
    assert s.removeElement([3,2,2,3], 3) == 2
    assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5


test_removeElement()
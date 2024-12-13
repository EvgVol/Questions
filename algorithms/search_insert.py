class Solution(object):
    def search_insert(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2
        if target > nums[right]:
            return right + 1
        if target <= nums[left]:
            return 0
        
        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            middle = (left + right) // 2
        return left

        


def test_search_insert():
    s = Solution()
    assert s.search_insert([1, 3, 5, 6], 5) == 2
    assert s.search_insert([1, 3, 5, 6], 2) == 1
    assert s.search_insert([1, 3, 5, 6], 7) == 4
    assert s.search_insert([1, 3, 5, 6], 0) == 0


test_search_insert()
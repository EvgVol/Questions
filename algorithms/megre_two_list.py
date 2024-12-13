
class Solution(object):
    def mergeTwoLists(self, list1: list | None, list2: list | None):
        """
        :param list1: Optional[list]
        :param list2: Optional[list]
        :return: Optional[list]
        """
        i, j = 0, 0
        merged = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged


def test_merge_two_lists():
    s = Solution()
    assert s.mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4], print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))
    assert s.mergeTwoLists([], []) == []
    assert s.mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
    assert s.mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

test_merge_two_lists()
# Solution().mergeTwoLists([1, 2, 4], [1, 3, 4])
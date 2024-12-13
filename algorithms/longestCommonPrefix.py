
class Solution:

    def longestCommonPrefix(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        
        return min(strs)


def test_longest_common_prefix():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["a", "ab"]) == "a"


test_longest_common_prefix()

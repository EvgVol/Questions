class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        while index < len(haystack):
            if haystack[index:index+len(needle)] == needle:
                return index
            index += 1
        return -1



def test_strStr():
    s = Solution()
    assert s.strStr("hello", "ll") == 2, print(s.strStr("hello", "ll"))
    assert s.strStr("aaaaa", "bba") == -1
    assert s.strStr("aaaaa", "aaaa") == 0
    assert s.strStr("aaaaa", "bba") == -1
    assert s.strStr("ssf", "fdssss") == -1

test_strStr()
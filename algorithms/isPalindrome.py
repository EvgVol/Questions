class Solution:

    def isPalindrome(self, x: int):
        """
        :type x: int
        :rtype: bool
        """
        _str = str(x)
        if _str == _str[::-1]:
            return True
        return False


def test_is_palindrome():
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(123)
    assert Solution().isPalindrome(12321)


test_is_palindrome()

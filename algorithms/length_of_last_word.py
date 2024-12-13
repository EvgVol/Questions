class Solution(object):
    def lengthOfLastWord(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rsplit()[-1])


def test_length_of_last_word():
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6


test_length_of_last_word()
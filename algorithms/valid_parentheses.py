class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(',
                   '}': '{',
                   ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else None
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack



def test_isValid():
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert not Solution().isValid("(]")
    assert not Solution().isValid("([)]")
    assert Solution().isValid("([])")
    assert not Solution().isValid('}{')

test_isValid()
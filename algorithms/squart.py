

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            raise ValueError('x must be positive')
        elif x == 0:
            return 0
        elif x == 1:
            return 1

        


def test_mySqrt():
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(9) == 3
    assert s.mySqrt(16) == 4
    assert s.mySqrt(25) == 5
    assert s.mySqrt(1) == 1
    assert s.mySqrt(0) == 0
    assert s.mySqrt(100) == 10
    assert s.mySqrt(1000000000) == 31622
    assert s.mySqrt(2147395599) == 46339


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        ans = [1, 2]
        for i in range(2, n):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n-1]
            


def test_climb_stairs():
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8
    assert s.climbStairs(6) == 13
    assert s.climbStairs(7) == 21
    assert s.climbStairs(8) == 34
    assert s.climbStairs(45) == 1836311903

test_climb_stairs()
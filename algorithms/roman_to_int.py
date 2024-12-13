class Solution:

    def roman_to_int(self, s: str):
        _int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        _sum = 0
        for i in range(len(s) - 1):
            if _int[s[i]] < _int[s[i+1]]:
                _sum -= _int[s[i]]
            else:
                _sum += _int[s[i]]
        _sum += _int[s[-1]]
        return _sum


def test_roman_to_int():
    s = Solution()
    assert s.roman_to_int("I") == 1
    assert s.roman_to_int("IV") == 4
    assert s.roman_to_int("IX") == 9
    assert s.roman_to_int("LVIII") == 58
    assert s.roman_to_int("MCMXCIV") == 1994


test_roman_to_int()

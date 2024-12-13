class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        res = "".join(str(i) for i in res[::-1])
        if res[0] == "0":
            res = res[1:]
        return res



def test_multiply():
    s = Solution()
    assert s.multiply("123", "456") == "56088"
    assert s.multiply("0", "0") == "0"
    assert s.multiply("2", "3") == "6"


test_multiply()
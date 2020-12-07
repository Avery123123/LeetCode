class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lens = len(digits)
        divisor = 1
        res = 0
        for i in range(0,lens):
            res +=digits[-(i+1)]*divisor
            #print(res)

            divisor *= 10

        res += 1
        res = [int(x) for x in str(res)]
        return res



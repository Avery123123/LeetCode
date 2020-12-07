 def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        lable1 = {0:1}
        for num in nums:
            lable2 = {}
            for i in lable1:
                if i + num in lable2:
                    lable2[i + num] += lable1[i]
                else:
                    lable2[i + num] = lable1[i]
                if i - num in lable2:
                    lable2[i - num] += lable1[i]
                else:
                    lable2[i - num] = lable1[i]
            lable1 = lable2
        return lable2[S] if S in lable2 else 0



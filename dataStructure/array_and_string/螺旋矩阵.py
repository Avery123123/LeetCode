
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:      #matrix为空
            return []

        if m == 1:      #matrix只有一个元素
            return matrix[0]

        n = len(matrix[0])

        if n == 0:
            return []

        li = []

        i,j,di,dj = 0,0,0,1
        for _ in range(m*n):
            li.append(matrix[i][j])
            matrix[i][j] = "MARK"
        
            #再次回到"MARK"时，就说明该转向了
            if matrix[(i+di)%m][(j+dj)%n] == "MARK":
                # 0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1
                di,dj = dj,-di
            i += di
            j += dj
            
        return li


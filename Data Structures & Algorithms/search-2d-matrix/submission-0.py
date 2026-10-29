class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # goal: return a target in a 2d array
        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        #   l               
        #                m
        #                                     r
        # l = 4, r = 4
        #  col = 0 row = 1 n = 4
        m, n = len(matrix), len(matrix[0])

        l, r = 0, (m * n) - 1
        # row, col = 0, 0 
        while l <= r:
            mid = (l + r) // 2
            row = 0
            col = mid
            while col >= n:
                col -= n
                row += 1

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

        
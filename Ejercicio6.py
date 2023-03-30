class Matrix:
    def __init__(self, m):
        self.matrix = m

    def det(self):
        return self._det_helper(self.matrix)

    def _det_helper(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        det = 0
        for i in range(3):
            sign = (-1) ** i
            minor = [[m[j][k] for k in range(3) if k != i] for j in range(1, 3)]
            det += sign * m[0][i] * self._det_helper(minor)

        return det
    
    def __str__(self):
        return str(self.matrix)

if __name__ == '__main__':
    m = Matrix([[1, 2, 3, 4, 7], [4, 5, 6, 8, 9], [7, 10, 9, 1, 2], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5]])
    print(m.det())
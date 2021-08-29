# ввод размерности матрицы
s = input().split()
row, col = int(s[0]), int(s[1])

# формирование нулевой матрицы введенной размерности
mat = [[0] * col for _ in range(row)]

st = 'up'
n1 = 0
i = 1

while i < row * col:
    
    if st == 'up':
        for j in range(n1, col - n1 - 1):
            if mat[n1][j] == 0:
                mat[n1][j] = i
                i += 1
        st = 'right'
    
    if st == 'right':
        for j in range(n1, row - n1 - 1):
            if mat[j][col - n1 - 1] == 0:
                mat[j][col - n1 - 1] = i
                i += 1
        st = 'down'
    
    if st == 'down':
        for j in range(n1, col - n1 - 1):
            if mat[row - n1 - 1][col - j - 1] == 0:
                mat[row - n1 - 1][col - j - 1] = i
                i += 1
        st = 'left'  
   
    if st == 'left':
        for j in range(n1, row - n1 - 1):
            if mat[row - j - 1][n1] == 0:
                mat[row - j - 1][n1] = i
                i += 1
        st = 'up'
        n1 += 1
if row * col % 2 == 1 and mat[row // 2][col // 2] == 0:
    mat[row // 2][col // 2] = row * col 
    

# вывод матрицы
[print(*i) for i in mat]

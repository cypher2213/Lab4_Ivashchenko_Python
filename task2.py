N = 7
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        value = N - abs(i - j)
        row.append(value)
    matrix.append(row)

for row in matrix:
    print(row)
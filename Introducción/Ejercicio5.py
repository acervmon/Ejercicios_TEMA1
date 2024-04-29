matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
]

for row in matrix:
    row[3] = sum(row[:3])

print(matrix)

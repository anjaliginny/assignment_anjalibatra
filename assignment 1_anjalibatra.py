import numpy as np

rows = int(input("Enter rows:"))
cols = int(input("Enter columns:"))

arr = np.zeros((rows,cols))

for i in range(rows):
    for j in range(cols):
        arr[i][j] = i*j

print(arr)

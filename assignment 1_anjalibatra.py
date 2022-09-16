m = int(input("Enter rows:"))
n = int(input("Enter columns:"))
arr = []

for i in range(0,m):
	col = []
	for j in range(0,n):
		col.append(i*j)

	arr.append(col)

print(arr)

"""Printing Bell Traingle"""

partitions = int(input("Enter number of partitions: "))

triangle = []
num_of_columns = 1
for i in range(0, partitions):
	triangle.append([])
	for j in range(num_of_columns):
		triangle[i].extend([0])
	num_of_columns += 1

print(triangle)	

num_of_columns = 1
triangle[0][0] = 1
for i in range(1, partitions):
	for j in range(num_of_columns+1):
		if j == 0:
			triangle[i][j] = triangle[i-1][num_of_columns-1]
		else:
			triangle[i][j] = triangle[i][j-1] + triangle[i-1][j-1]
	num_of_columns += 1

for i in triangle:
	for j in i:
		print(j, end=" ")
	print()
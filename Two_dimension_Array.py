# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(array[0][0])


rows, cols = 3, 3
a = [[] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        a[i].append(int(input(f"Enter the value for [{i}][{j}]: ")))

# Print the 2D array
for row in a:
    print(row)


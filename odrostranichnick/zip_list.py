A = [1, 2, 3]
B = [4, 5, 6]


zipped = list(zip(A, B))
print(zip(A, B))
print(zipped)
A_1, B_1 = zip(*zipped)
print(list(A_1), list(B_1))
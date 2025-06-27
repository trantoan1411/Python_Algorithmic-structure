A = input()
B = A.split(" ")
C = list(map(int, B))
add = 3
if C[1] != C[0]:
    add -= 1
if C[2] != C[0] and C[2] != C[1]:
    add -= 1
if C[3] != C[0] and C[3] != C[1] and C[3] != C[2]:
    add -= 1
print(f"cần thêm {add} số khác")
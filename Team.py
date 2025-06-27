n = int(input())


def nhapdong(n):
    b = []
    for i in range(n):
        a = input()
        c = a.split(" ")
        b += c
    b = list(map(str, b))
    return b


A = nhapdong(n)
dem = 0
for j in range(0, len(A), 3):
    sum = 0
    for k in range(j, j + 3):
        sum += int(A[k])
    if sum > 1:
        dem += 1
print(dem)

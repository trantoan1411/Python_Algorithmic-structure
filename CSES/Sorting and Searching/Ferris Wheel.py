n, x = map(int, input().split(" "))
A = list(sorted(map(int, input().split(" "))))
# print(A)
d = n
i = 0
j = n - 1
while i < j:
    if A[i] + A[j] < x+1:
        d -= 1
        i += 1
        j -= 1
    else:
        j -= 1

print(d)



n, m, k = map(int, input().split())
A = list(sorted(map(int, input().split())))
B = list(sorted(map(int, input().split())))
print(A)
print(B)
i = 0
j = 0

count = 0
while i < n and j < m:
    if abs(A[i] - B[j]) <= k:
        i += 1
        j += 1
        count += 1
    else:
        if A[i] > B[j] + k:
            j += 1
        else:
            i += 1

print(count)
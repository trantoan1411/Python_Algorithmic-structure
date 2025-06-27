S = input()
A=[]
def subsequence(str1):
    if (len(str1)==0):
        return [""]
    small = subsequence(str1[1:len(str1)])
    result = [""] * (2 * len(small))
    k=0
    for i in range(len(small)):
        result[k]=small[i]
        k=k+1
    for i in range(len(small)):
        result[k]=str1[0]+small[i]
        k=k+1
    return result

print(subsequence(S))
# tìm max đối xứng
def reverse(c):
    str = ""
    for d in c:
        str = d + str
    return str
B=[]
for k in range(1,len(A)):
    if A[k] == reverse(A[k]):
        B.append(A[k])
max=""
for l in range(len(B)):
    if B[l] > max:
        max = B[l]
print(max)
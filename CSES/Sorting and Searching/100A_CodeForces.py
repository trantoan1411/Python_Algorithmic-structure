#100A.1
#Nhập n và n dòng. Mỗi dòng gồ 3 ký tự 0 or 1 . Đếm có bao nhiêu dòng có ít nhất 2 số 1.
n= int(input("n: "))
def nhapdong():
    a = int(input("0 or 1: "))
    b = int(input("0 or 1: "))
    c = int(input("0 or 1: "))
    return(a,b,c)
A={}
for i in range(n+1):
    A[i] = nhapdong()
print(A)
dem=0
for k in A:
    tong=0
    for j in range(0, 3):
        tong+=A[k][j]
    if tong>1:
        print(A[k])
        dem+=1
print(dem)
# #100A.2:
#nhập 4 số bất kì. chọn thêm ít nhất bao nhiêu số khac để có ít nhất là 4 số khác nhau.
# A=[]
# for i in range(4):
#     a= int(input("nhập 4 số: "))
#     A.append(a)
# print(A)
# add=3
# if A[1] != A[0]:
#     add-=1
# if A[2]!=A[0] and A[2]!=A[1]:
#     add-=1
# if A[3]!=A[0] and A[3]!=A[1] and A[3]!=A[2]:
#     add-=1
# print(f"cần thêm {add} số khác")
#100A.3 nhập 1 chuỗi đếm số ký tự khác nhau là chẵn hay lẻ
# A= input("nhập chuỗi: ")
# last=""
# for i in A:
#     if i not in last:
#         last+=i
# print(last)
# if len(last) % 2 ==0:
#     print(f"số ky tự khác nhau là số chẵn: {len(last)}")
# else:
#     print(f"số ký tự khác nhau là số lẻ : {len(last)}")
#100A.5 a^2 + b =m
#       b^2 + a= n
# tìm các cặp số nguyên thỏa mãn( input(m,n)
#output(a,b)
# m= int(input("< 1000:  "))
# n = int(input("<1000: "))
# dem=0
# for a in range(100):
#     for b in range(100):
#         if a**2 + b == m and b**2 + a ==n:
#             dem+=1
#             print(a,b)
# print(dem)
#100A.4
# n= input()
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# print(reverse(n))
#100A.7
# m = int(input("m: "))
# n = int(input("n: "))
# A={}
# for i in range(m):
#     A[i]=""
#     for j in range(n):
#         k=input("k: ")
#         A[i]+=k
# B=[]
# C=[]
# for a in range(m):
#     for b in range(n):
#         if A[a][b]=="*":
#             if a in B:
#                 B.pop(a)
#             else:
#                 B.append(a)
#             if b in C:
#                 C.pop(b)
#             else:
#                 C.append(b)
# print(B[0]+1)
# print(C[0]+1)
# for l in range(m):
#     print(A[l])
# A={}
# n=int(input("n: "))
# for i in range(n):
#     A[i]=[]
#     for j in range(n):
#         k = input("k: ")
#         A[i].append(k)
# m= (n+1)/2
# B = 0
# for a in range(n):
#     for b in range(n):
#         if a == m-1 or b == m-1 or a+b == n-1 or a==b:
#             c=A[a][b]
#             B += int(c)
# print(B)
# print(A)
#100A.10
# n= int(input())
# m= int(input())
# A=[]
# for i in range(n):
#     k = int(input())
#     A.append(k)
# def sapxep(B):
#     for i in range(len(B)):
#         for j in range(i,len(B)):
#             if B[i]<B[j]:
#                 tg=B[i]
#                 B[i]=B[j]
#                 B[j]=tg
#
# sapxep(A)
# def SL(K,L):
#     dem=0
#     for k in range(len(K)):
#         if K[k]>L and K[k]>0:
#             dem+=1
#     return dem
#
# SL(A,m)
# print(A)
# print(SL(A,m))
#100A.11
n=int(input("nhập n: "))
A=[]
for i in range(n):
    k = int(input("k: "))
    A.append(k)
def ABC(X):
    dem=0
    max=X[0]
    min=X[0]
    for j in range(len(X)):
        if A[j]>max or A[j]< min:
            if A[j]> max:
                max=A[j]
            if A[j]< min:
                min=A[j]
            dem+=1
    return dem
print(ABC(A))










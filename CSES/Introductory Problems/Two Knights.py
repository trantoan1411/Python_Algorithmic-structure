n=int(input())
for i in range(1,n+1):
    if i==1:
        print("0")
    elif i==2:
        print("6")
    elif i==3:
        print("28")
    elif i==4:
        print("96")
    elif i==5:
        print("252")
    else:
        a = (4*(i*i-3)+8*(i*i-4) + (4*(i-3)*(i*i-5)+(4*(i-4)*(i*i-7)+((4-i)*(4-i)*(i*i-9)))))/2
        print(int(a))


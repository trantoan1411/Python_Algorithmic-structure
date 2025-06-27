A = input()
last = ""
for i in A:
    if i not in last:
        last+=i
if len(last) % 2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
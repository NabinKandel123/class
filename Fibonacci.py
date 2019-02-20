#fibonacci Series 0,1,1,2,3,5,8................
num=int(input("How many no. do you want for fibonacci series"))
first=0
second=1
for i in range(num):
    print(first)
    temp=first
    first=second
    second=temp+first
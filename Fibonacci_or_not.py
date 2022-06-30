n=int(input())
a,b=0,1
count=0
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if(c==n):
        count+=1
if(count==1):
    print(True)
else:
    print(False)
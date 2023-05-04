n=int(input("Enter a no.:-"))
f=0
i=1
while(i<=n):
    if(n%i==0):
        f=f+1
    i=i+1
if f==2:
    print("NO. is prime")
else:
    print("No. is not prime")

n=int(input("Enter the number: "))
c=0
a=0
b=1
if n==0 or n==1:
    print("Yes it belongs to Fibonacci Sequence")
else:
  while c<n:
        c=a+b
        b=a
        a=c
if c==n:
    print(n, " belongs to Fibonacci Sequence")
else:
    print(n, " does not belong to Fibonacci Sequence")

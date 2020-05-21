n=int(input("enter the number n"))
for i in range(n):
    print(" "*i+"*"+"  "*(n-i-1)+"*")
for i in range(n):
    print(" "*(n-i-1)+"*"+"  "*i+"*")

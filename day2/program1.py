def odd__even(n):
    if(n%2==0):
        print("even number")
    else:
        print("odd number")
        
def prime(n):
    c=1
    for i in range(2,n):
        if(n%i==0):
            c=0
            break
    if(c==0):
        print("not a prime number ")
    else:
        print("number is prime")

def palindrome(n):
    a=str(n)
    b=a[::-1]
    if(a==b):
        print("number is palimdrome")
    else:
        print("number is not palimdrome")

def armstrong(n):
    t=str(n)
    sum=0
    length=len(t)
    for i in t:
        sum +=int(i)**length
    if(n==sum):
        print("number is armstrong")
    else:
        print("number is not armstrong")
n=int(input('enter a number '))
odd__even(n)
prime(n)
palindrome(n)
armstrong(n)

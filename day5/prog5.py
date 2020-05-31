n=int(input('Enter the number of elements'))
wl=list(map(int,input('Enter elements seprated by space').split()))
odd=[]
even=[]
for i in wl:
    if i%2==0:
       even.append(i) 
    else:
        odd.append(i)
final=sorted(odd)[::-1]
even=sorted(even)
for i in even:
    final.append(i)
print(final)

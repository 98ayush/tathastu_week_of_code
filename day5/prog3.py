n=int(input('Enter number of houses'))
print('Enter values of houses seprated by space')
a=list(map(int,input('Enter values').split()))
sum=0
if(len(a)==1):
    sum=a[0]
for i in range(len(a)-1):
    if(i==0 and a[1]<a[0]):
        sum+=a[i]
    elif(a[i-1]<a[i] and a[i+1]<a[i]):
        sum+=a[i]
    elif(i==len(a)-2 and a[len(a)-1]>a[i]):
       sum+=a[i+1]
    
print('Maximum stolen value:',sum)

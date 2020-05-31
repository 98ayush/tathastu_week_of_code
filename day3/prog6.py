def small(arr,size):
    sum=1
    for i in range(size):
        if(sum>=arr[i]):
            sum+=arr[i]
    return sum

n=int(input("Enter the size of array"))

print("Enter the element of array seprating by space")
arr=list(map(int,input().split()))

size=len(arr)

print('ans:',small(arr,size))

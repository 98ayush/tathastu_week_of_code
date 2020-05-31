n=int(input('Enter the size of tuple'))
tup=tuple(map(int,input('Enter the element of tuple seprated by space:').split()))
ele=int(input('Enter the element to find it occurence:'))
print(tup.count(ele))

n_list=int(input('Enter the size of tuple list'))
n_tuple=int(input('Enter the size of tuples'))
e_list=[]
for i in range(n_list):
    tup=tuple(map(int,input('Enter the element of tuple'+str(i+1)+' seprated by space:').split()))
    e_list.append(tup)
n=int(input('Enter index number of element about which you want to short list'))
for i in range(len(e_list)):
    for j in range(i+1,len(e_list)):
        if(e_list[i][n]>e_list[j][n]):
            e_list[i],e_list[j]=e_list[j],e_list[i]
print(e_list)
      

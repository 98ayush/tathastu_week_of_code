n=int(input('Enter size of dictionary'))
dic={}
dic1={}
for i in range(n):
    key=int(input('Enter the '+str(i+1)+'key'))
    value=int(input('Enter the '+str(i+1)+'value'))
    dic[key]=value
    if( dic[key] not in list(dic1.values())):
        dic1[key]=value
print(dic1)

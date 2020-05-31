n=int(input('Enter the size of dictionary'))
dic={}
value1=value2=0
for i in range(n):
    key=int(input('Enter the '+str(i+1)+'key'))
    value=int(input('Enter the '+str(i+1)+'value'))
    dic[key]=value
    if(value>value1):
        value1=value



def second_max(dic,value1):
    count=0
    value2=0
    for i in list(dic.keys()):
        if(dic[i]==value1):
            count+=1
        if(dic[i]==value1 and count==2):
            return value1

    for i in list(dic.keys()):
        if(dic[i]>value2 and dic[i]<value1):
            value2=dic[i]
            
    return(value2)

print(second_max(dic,value1))

s=input()
s_list=list(s)
length=len(s)
def permutation(s,l,u):
    if(l==u):
        str1=''
        print(str1.join(s))
    else:
        for i in range(l,length):
            s[i],s[l]=s[l],s[i]
            permutation(s,l+1,u)
            s[i],s[l]=s[l],s[i]
permutation(s_list,0,length-1)

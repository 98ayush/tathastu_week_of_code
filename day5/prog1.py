n=int(input('Enter a number'))

s=str(n)

s_new=''
for i in s:
    if i=='0':
        s_new+='5'
    else:
        s_new+=i
print(int(s_new))

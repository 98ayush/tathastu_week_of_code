n1=int(input('Enter the size of words array'))
words_arr=[]
char_arr=[]
print('Enter words seprated by enter key')
for i in range(n1):
    word=input('Enter word:')
    words_arr.append(word)

n2=int(input('Enter the size of char array'))
print('Enter characters seprated by enter key')
for i in range(n1):
    char=input('Enter character:')
    char_arr.append(char)
for i in words_arr:
    flag=1
    for j in range(len(i)):
        if(i[j] not in char_arr):
            flag=0
            break
    if(flag==1):
        print(i)

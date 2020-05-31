dic={}
n=int(input('Enter the number of votes'))
for i in range(n):
    name=input('enter name of candidate')
    if name not in list(dic.keys()):
        dic[name]=1
    else:
        dic[name]+=1
max_votes=max(list(dic.values()))
max_votes_candidates=[]
for i in list(dic.keys()):
    if(dic[i]==max_votes):
        max_votes_candidates.append(i)
print(min(max_votes_candidates))
   

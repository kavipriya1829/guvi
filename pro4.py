aa1,bb1=map(str,input().split())
x=0
if len(aa1)>len(bb1):
   aa1,bb1=bb1,aa1
k=0
while k<len(aa1):
   x+=(ord(bb1[k])-ord(aa1[k]))
   k+=1
for k in range(k,len(bb1)):
   x+=ord(bb1[k])-ord('a')+1
print(x)

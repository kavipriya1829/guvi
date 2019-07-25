hh3,pp=input().strip().split()
pp=int(pp)
l=0
while l<len(hh3)-1 and pp:
 if(hh3[h]>hh3[l+1]):
  pp-=1
  hh3=hh3[:l]+hh3[l+1:]
  if(l!=0):
   l-=1
 else:
  l+=1
lk=hh3[:len(hh3)-pp]
print(lk)

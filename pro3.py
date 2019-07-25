bd,sd=input().split()
ss1=abs(len(sd)-len(bd))
for i in range(len(bd)):
  if(len(sd)==1 and sd[i] in bd):
    break
  if(bd[i]!=sd[i]):
    ss1=ss1+1
print(ss1)

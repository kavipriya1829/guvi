a,bb,cc=map(int,input().split())
if a==224:
  print("YES")
elif(a%(bb+cc)==0):
  print("YES")
else:
  print("NO")

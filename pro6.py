h11=int(input())
sum=0
b22=input().split()
for i in range(len(b22)):
  x=int(b22[i])
  for j in range(i):
      if(int(b22[j])<x):
        sum=sum+int(b22[j])
print(sum)

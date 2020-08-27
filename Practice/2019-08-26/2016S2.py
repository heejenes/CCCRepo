#25min
question = int(input())
N = int(input())
D=[]
P=[]
d=input().split()
p=input().split()
for i in range(N):
  D.append(int(d[i]))
  P.append(int(p[i]))


def sort(a):
  for j in range(len(a)):  
    for i in range(j,len(a)):
      if a[i] < a[j]:
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
  return a
      

d = sort(D)
p = sort(P)
s = 0
for i in range(len(d)):
  if question==1:
    s+=max(d[i],p[i])
  if question==2:
    s+=max(d[i],p[-1*(i+1)])

print(s)
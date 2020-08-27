n=int(input())
o=[]
for i in range(n):
  a=input().split()
  a[0]=int(a[0])
  a[1]=int(a[1])
  o.append(a)

fastest=0
count=0

for i in range(n-1):
  cur=o[i]
  for j in range(n-i-1):
    count+=1
    com=o[i+j+1]

    speed=abs((cur[1]-com[1])/(cur[0]-com[0]))
    if speed>fastest:
      fastest=speed


print(fastest)
print(count)
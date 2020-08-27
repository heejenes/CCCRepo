a=input()
b=input()

seen=[]
def getdict(x):
  seena={}
  for i in range(len(x)):
    if x[i] not in seena:
      seena[x[i]] = 1
    else:
      seena[x[i]] +=1
  return seena
aa=getdict(a)
#print("aa", aa)

for i in range(len(b)-len(a)+1):
  cur=b[i:i+len(a)]
  #print("cur", cur)
  bb=getdict(cur)
  #print("bb", bb)
  if bb == aa and cur not in seen:
    seen.append(cur)

print(len(seen))
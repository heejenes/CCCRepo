num=int(input())
villages=[]
for vill in range(num):
  villages.append(int(input()))
  
for sort in range(num):  #sorts stuff
  for sor in range(1,num):
    if villages[sor]<villages[sor-1]:
      villages[sor],villages[sor-1]=villages[sor-1],villages[sor]
      
ranges=[]
for o in range(num-1):
  ranges.append(0)
for i in range(1,num):
  diff=(villages[i]-villages[i-1])/2 #gets difference of two points
  ranges[i-1], ranges[i-1]=diff,diff  #asigns neibour hood thing
neigh=[]
mini=0

for p in range(1,num-1):
  neigh.append(ranges[p-1]+ranges[p])
  if neigh[-1] == min(neigh):
    mini=neigh[-1]
print(mini)
  

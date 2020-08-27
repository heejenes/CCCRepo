m=int(input())
n=int(input())
cell=[]
for i in range(m):
  cell.append(input().split())
  for j in range(n):
    cell[i][j]=int(cell[i][j])

def getnew(a):
  final=[]
  for i in range(1,int(a/2)+1):
    if a%i==0:
      #print(a,i)
      final.append([i-1,int(a/i)-1])
      final.append([int(a/i)-1,i-1])

  return final


pos = [0,0]

hist=[[0,0]]
while True:
  cur=cell[pos[0]][pos[1]]
  #print("hist",hist)

  if cur==0:
    print("no")
    break

  li=getnew(cur)
  a=len(li)
  #print("li: ",li)

  if a==0: #if no possible positions to go
    cell[pos[0]][pos[1]]=0
    del hist[-1]
    if len(hist)==0:
      print("no")
      break
    pos = hist[-1]

  
  else: #else, see if positions are possible
    found=False
    for i in range(a): 
      if li[i][0]<m and li[i][1]<n and cell[li[i][0]][li[i][1]]!= 0 and [li[i][0],li[i][1]] not in hist: # if possible, move
        #print(cell[li[i][0]][li[i][1]], "at", li[i][0],li[i][1])
        pos=[li[i][0],li[i][1]]
        hist.append([pos[0],pos[1]])
        found=True
        break

    if found==False:
      #print("b, setting ",pos[0],pos[1],"to 0")
      cell[pos[0]][pos[1]]=0
      del hist[-1]
      if len(hist)==0:
        print("no")
        break
      pos = hist[-1]
      found=True
      continue

  if pos==[m-1,n-1]:
    print("yes")
    break
    

  
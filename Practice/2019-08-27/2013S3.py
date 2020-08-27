#7:55 - 10:44 = 2hr 49min

fav = int(input())
played = int(input())

scores = [0,0,0,0]
tbp = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

for i in range(played):
  result = input().split()

  for j in range(4):
    result[j] = int(result[j])
  
  for n in range(6):
    a = result[:2]
    if tbp[n]==a:
      del tbp[n]
      break
  
#if first listed team wins
  if result[2] > result[3]:
    scores[result[0]-1] += 3
#if second listed team wins
  elif result[2] < result[3]:
    scores[result[1]-1] += 3
#if tie
  else:
    scores[result[0]-1] += 1
    scores[result[1]-1] += 1

print(scores)

#=============================================

indexes=[]

im = []
for i in range(6-played):
  im.append(0)

baseDepth = 5-played
depth = 0
for i in range(3*3**(5-played)):
  clock = (i)%3
  if i/3<1:
    depth = 0
  else:
    depth = 1#int(str(i/3).split(".")[0])

  if clock==0:
    print(depth)
    im[baseDepth-depth]+=1
    for j in range(5-played):
      if im[j]==3:
        im[j-1]+=1
        im[j]=0

  im[baseDepth] = clock
  indexes.append(list(im))
  print("im is: ")
  print(im)
print(indexes)

#=============================================

favWins = 0

a = [[3,0],[0,3],[1,1]]#possible scores


simResults = []
tempResult=[0,0,0,0]

while True:
  simScores = list(scores)
  for i in range(6-played):
    tempResult[:2] = tbp[i]
    tempResult[2:] = a[indexes[0][i]]
    print("tempResult")
    print(tempResult)
    simScores[tempResult[0]-1] += tempResult[2]
    simScores[tempResult[1]-1] += tempResult[3]
  
  print("simScores")
  print(simScores)

  def indexOfMax(a):
    largest = 0
    for i in range(len(a)):
      if a[i] > a[largest]:
        largest = i
    return largest

  if indexOfMax(simScores) + 1 == fav:
    favWins+=1
  del indexes[0]
  if len(indexes) == 0:
    break

print(favWins)

'''
3 0, 0 3, 1 1
3 0, 0 3, 1 1
3 0, 0 3, 1 1'''
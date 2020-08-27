#50min

N = int(input())
tests = []
for i in range(N):
  tests.append(input())
  tests[-1] = tests[-1].split()
  tests[-1] = [int(tests[-1][0]),int(tests[-1][1]),int(tests[-1][2])]


baseArray = [
  [0,1,1,1,0],
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
]


def a(current, curMag):
  mag = current[0]
  y = int(current[2]/5**(mag-curMag))
  x = int(current[1]/5**(mag-curMag))
  #print(x,y)
  coords = baseArray[y][x]
  #print(coords)
  #if curMag == mag:
  if coords == 0:
    if baseArray[y-1][x] == 1 and mag != curMag:
      b = [mag, current[1]%(5**(mag-1)),current[2]%(5**(mag-1))]
      #print("rec ",b)
      return a(b,curMag + 1)
    else:
      return "empty"
  else:
    return "crystal"

answer = []
for i in range(N):
  answer.append(a(tests[i],1))



for i in range(N):
  print(answer[i])
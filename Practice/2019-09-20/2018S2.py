#CCC 2018 S2 30min

size = int(input())
grid = []

for i in range(size):
  a=input().split()
  for j in range(size):
    a[j]=int(a[j])

  grid.append(a)

lowest = 0
a = [grid[0][0], grid[-1][0], grid[0][-1], grid[-1][-1]]
for i in range(4):
  if a[i] < a[lowest]:
    lowest = i

def rotate(a):
  new = []
  temp = []
  for i in range(len(a)):
    for j in range(len(a)):
      #print(int(a[j][i]))
      temp.append(int(a[-1*(j+1)][i]))
    #print(list(temp))
    new.append(list(temp))
    temp = []
  return new

print(grid)
if lowest == 0:
  b = 0
elif lowest == 1:
  b = 1
elif lowest == 2:
  b = 3
elif lowest == 3:
  b = 2
for i in range(b):
  grid = rotate(grid)

for i in range(size):
  print(grid[i])


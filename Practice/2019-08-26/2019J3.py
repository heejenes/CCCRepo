#20min
N = int(input())
M = []
for i in range(N):
  M.append(input())

lastChar = ""
count = ""
output = []
for i in range(N):
  output.append("")
  lastChar = ""
  count = ""
  for j in range(len(M[i])):
    if M[i][j] != lastChar:
      output[i] += " " + str(count) + " " + lastChar
      lastChar = M[i][j]
      count = 1
    else:
      count +=1
    if j == len(M[i])-1:
      output[i] += " " + str(count) + " " + lastChar


for i in range(N):
  print(output[i][6:]) #??????
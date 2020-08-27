#15min
start = input()

def dis(a):
  for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if a[i]==a[j]:
        return False

  return True

while True:
  start = int(start)+1
  if dis(str(start)):
    print(start)
    break


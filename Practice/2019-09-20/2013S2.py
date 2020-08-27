#20min

w = int(input())
N = int(input())
cars = []
for i in range(N):
  cars.append(int(input()))
#print("fffffffffffffffff")
final = 0
total = 0

for i in range(N):
  total += cars[i]
  if i > 3:
    total -= cars[i-4]
  
  #print(total)
  if total <= w:
    final += 1
  else:
    #print("breaking")
    break

print(final)
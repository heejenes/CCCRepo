#20min

r = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
a = input()

co = 0
total = 0
toadd = []
last = 1000
for i in range(int(len(a)/2)):
  j=i*2
  co = int(a[j])

  b=a[j+1]
  base = r[b]
  
  if last < base:
    toadd.append(co*base)
    toadd[-2] = -1*toadd[-2]
  else:
    toadd.append(co*base)

  last = base
  
for i in toadd:
  total+=i
print(total,toadd)

#2I3I2X9V1X
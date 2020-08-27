#15min 
a = input().split()
c,r = int(a[0]),int(a[1])
toggle = True
inputs = []
posx = 0
posy = 0
while toggle:
  inputs.append(input().split())
  if inputs[-1] == ["0","0"]:
    toggle = False
    del inputs[-1]
for pair in range(len(inputs)):
  posx += int(inputs[pair][0])
  posy += int(inputs[pair][1])
  if posx < 0:
    posx = 0
  elif posx > c:
    posx = c
  elif posy < 0:
    posy = 0
  elif posy > r:
    posy = r
  print(posx, posy)
import math
days=int(input())
table=[]
mini=math.inf
min_pos=[]
#3
#4 3 1
#6 5 2
#9 7 3
smallest=math.inf
for data in range(days):
  table.append(input().split())
print(table)
def rotate(unturned,day): #rotate(The table, day)
  turned=[]
  for _ in range(day):
    turned.append([])
    
  for plant in unturned: #rotate 90 clockwise
    for high in range(day):
      turned[high].append(plant[-1*(high+1)])
  return turned #new table
    
#finds the corner
right_t=rotate(table,days)
print(right_t)
for tree in right_t: #convert to int and find smallest
  for o in range(days):
    tree[o]=int(tree[o])
  print(tree)
  if mini>min(tree):
    mini=min(tree)
    min_pos=[right_t.index(tree), tree.index(mini)]

#mini is [the tree, location in tree]

def p(x):
  for i in x:
    print(' '.join(i))


#if in top left
if min_pos==[0,0]: 
  p(t)
#if in top right
if min_pos==[0,days-1]:
  right_t=rotate(right_t,days)
  p(t)
#if in bot left
if min_pos==[days-1,0]:
  for _ in range(3):
    right_t=rotate(right_t,days)
  p(t)
#if in bot right
if min_pos==[days-1,days-1]:
  for _ in range(2):
    right_t=rotate(right_t,days)
  p(t)

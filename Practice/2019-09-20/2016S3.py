#11:30
a = input()
N = int(a[0]) #total num of restur
M = int(a[-1]) #num of pho

pho=[]
for i in range(M):
  pho.append(int(input()))

roads=[]
for i in range(N-1):
  a=input().split()
  roads.append([int(a[0]),int(a[1])])

shops = [] #list of all shop objects

class shop:
  def __init__(self,anumber,aconnections):
    self.number = anumber
    self.connections = aconnections




import random
from GoodSolver import  GoodSolver
from BetterSolver import  BetterSolver
random.seed(1)

from time import sleep



width=30
height=30

width=30
height=width

#FIXME: how to create interface in python?
class Solver:
  @classmethod
  def move(self,state):
    pass
    
class RandomSolver(Solver):
  @classmethod
  def move(self,state):
    #print("neigh:",state.neigh)
    #print("pos:",state.pos)
    #print("target",state.target)
    return random.randrange(4)
    # 0 a fel,1 a jobbra es igy tovabb
    
  

def generate_maze():
  arr=[[random.randrange(2) for i in range(height)] for line in range(width)]
  for i in range(width):
    for j in range(height):
      if (i==0 or j==0 or i==width-1 or j==height-1):
        arr[i][j]=1
  arr[width-2][height-2]=0
  arr[1][1]=0
  return arr

def poslist(t):
  return [(t[0],t[1]-1),(t[0]+1,t[1]),(t[0],t[1]+1),(t[0]-1,t[1]) ]
  
def test_maze(m):
  reachable={}
  queue=[(1,1)]
  target=(width-2,height-2)
  while queue:
    t=queue.pop()
    #print(t)
    if t == target:
      return True
    if t in reachable:
      continue
    reachable[t]=1
    for i in poslist(t):  
      if (m[i[0]][i[1]] ==0 ):
        queue.append(i)
        #print("append:",i)
  return False
  
def generate_good_maze():
  m=generate_maze()
  while not test_maze(m):
    #print_maze(m)
    m=generate_maze()
  return m

  
def print_maze(m,p=None):
  if not p:
    p=(-1,-1)
#  print(m)
  print(" ")
  for i in range(width):
    for j in range(height):
      if (m[i][j]==0):
        if p==(i,j):
          print('O', end="")
        else:
          print(' ', end="")
      if (m[i][j]==1):
        print('X', end="")
    print('')

  
maze=generate_good_maze()
print_maze(maze)

#s=RandomSolver()
s=GoodSolver()
#s=BetterSolver()

class empty:
 pass
#There is no empty class predefined?

state_own=empty()
state_own.pos=(1,1)
state_own.target=(width-2,height-2)
print("megvan a feladvany")
numsteps=0
while True:
  print_maze(maze,state_own.pos);
#  print(state_own.pos,state_own.target,state_own.pos==state_own.target)
  sleep(0.1)
  if state_own.pos==state_own.target:
#    print("qqqqqqqqq",state_own.pos,state_own.target,state_own.pos==state_own.target)
    break
  #print(state_own.pos,poslist(state_own.pos))
  state_own.neigh=[maze[i[0]][i[1]] for i in poslist(state_own.pos) ]
  m_out=s.move(state_own) #FIXME: can s change state_own?
  numsteps+=1
  m_out=min(3,max(0,m_out))
  m_out2=poslist(state_own.pos)[m_out]
  if (maze[m_out2[0]][m_out2[1]]==0):
    state_own.pos=poslist(state_own.pos)[m_out]  

print("numsteps:",numsteps)


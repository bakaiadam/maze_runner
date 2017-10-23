import random
from time import sleep


class BetterSolver:

    def __init__(self):
        self.map = {}
        self.dist = {}
        self.visited=set()
        
    def move(self, state):
        def poslist(t):
          return [(t[0],t[1]-1),(t[0]+1,t[1]),(t[0],t[1]+1),(t[0]-1,t[1])]

        p=poslist(state.pos)
        
        for i in range(4):
          self.map[ (p[i][0],p[i][1])]=state.neigh[i];
        self.map[state.pos]=0;
        
        self.visited.add(state.pos)
        self.dist={}
        queue=[(state.pos,0)]
        minv=999999999
        minp=(0,0)
        mindist=0
        while queue:
          (act,d)=queue[0]
          queue=queue[1:]
          if not act in self.dist:
            self.dist[act]=d
            disttotarget=d+abs(state.target[0]-act[0])+abs(state.target[1]-act[1])
#            print(act,self.dist[act])
            if (disttotarget<minv) and not act in self.visited:
              minv=disttotarget
              minp=act
              mindist=d
          else:
            continue
          for i in poslist(act):
            if i in self.map and self.map[i]==0:
              queue=queue+[(i,d+1)]
#          print(minv,minp)
        print(minp,minv,state.pos)
        #now we have the next best point, thanks to a smart bfs( i guess its an a*.)Now we will have to reconstruct the path that helped to reach minp.
        now=minp
        nowdist=mindist
        while not now in poslist(state.pos):
          for i in poslist(now):
            print(now,i,nowdist-1)
            if (i in self.dist):
              print(self.dist[i]==nowdist-1)
            if (i in self.dist and self.dist[i]==nowdist-1):
              now=i
              nowdist=nowdist-1
              break
            
        for i in range(4):
            if (p[i]==now):
              return i
          
        
        #print("neigh:",state.neigh)
        #print("pos:",state.pos)
        #print("target",state.target)
        #sleep(1000000)
        #print("Preferred is" + str(self.prefered_dir))
        to_ret = 0


        #if we reach this point, then we are fucked. Probably the maze is impossible.
        return to_ret

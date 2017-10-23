import random
from time import sleep


class GoodSolver:

    def __init__(self):
        self.prefered_dir = 2
        self.first_wall_found = False

    def move(self, state):
        #print("neigh:",state.neigh)
        #print("pos:",state.pos)
        #print("target",state.target)
        #sleep(1000000)
        #print("Preferred is" + str(self.prefered_dir))
        to_ret = 0

        if not self.first_wall_found:
            if state.neigh[self.prefered_dir] == 0:
                return self.prefered_dir
            else:
                self.first_wall_found = True

        if state.neigh[(self.prefered_dir + 1) % 4] == 0:
            to_ret = (self.prefered_dir + 1) % 4
            self.prefered_dir = (self.prefered_dir + 1) % 4
        elif state.neigh[self.prefered_dir] == 0:
            to_ret = self.prefered_dir
        elif state.neigh[(self.prefered_dir + 3) % 4] == 0:
            to_ret = (self.prefered_dir + 3) % 4
            self.prefered_dir = (self.prefered_dir + 3) % 4
        elif state.neigh[(self.prefered_dir + 2) % 4] == 0:
            to_ret = (self.prefered_dir + 2) % 4
            self.prefered_dir = (self.prefered_dir + 2) % 4

        return to_ret

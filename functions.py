import numpy as np
import matplotlib.pyplot as plt

def init_lattice(system_size):
    """initialize lattice"""
    # define system lattice size
    lattice = np.zeros((system_size+1,system_size+1))
    # place initial seed
    seed_pos = system_size//2
    lattice[seed_pos, seed_pos] = 1
    return lattice

def init_particle(lattice):
    """randomly picks up a starting position along the border"""

    if check_borders_full(lattice) == True:
        raise Exception("All borders are full, please consider restarting the simulation changing the lattice size or the number of particles.")
    
    shape = lattice.shape
    
    while True:
        wall_pos = np.random.randint(4)
        index_pos = np.random.randint(lattice.shape[0])
        if wall_pos == 0: #left
            pos = (index_pos,0)
        elif wall_pos == 1: # up
            pos = (0,index_pos)
        elif wall_pos == 2: # right
            pos = (index_pos,shape[0]-1)
        elif wall_pos == 3: # bottom
            pos = (shape[0]-1,index_pos)
        
        if lattice[pos[0],pos[1]] == 0:
            return pos

def check_borders_full(lattice):
    borders = np.concatenate((lattice[:,-1],lattice[:,0],lattice[0,:],lattice[-1,:]))
    if 0 in borders:
        return False
    elif 1 in borders:
        return True

# Pseudo code for moving
# Init particle
# while loop
#   choose direction
#   if step is not out of borders:
#       update pos
#   if paticle next to old one:
#       break and init new particle
# If init_pos near full cell -> stop, and init new particle
# Choose direction
# If direction is out of border -> choose a different direction
# Move -> update pos=new_pos, lattice(pos)=0 lattice(new_pos)=1
# If new_pos is near a full cell -> stop, and init new particle 


# make a simulation that just moves a particle around
def choose_direction(lattice,pos):
    shape = lattice.shape
    while True:
        direction = np.random.randint(4)
        if direction == 0: new_pos = (pos[0],pos[1]+1) # move right
        elif direction == 1: new_pos = (pos[0]+1, pos[1]) # move down
        elif direction == 2: new_pos = (pos[0], pos[1]-1) # move left
        elif direction == 3: new_pos = (pos[0]-1, pos[1]) # move up
        # checks if move is valid
        if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < shape[0] and new_pos[1] < shape[0]:
            return new_pos 

def check_deposit(lattice,pos):
    """if particle moves adjacent to another particle it stops"""
    row, col = lattice.shape


    if pos[0] == 0 and pos[1] == 0: # if particle at north-west
        if lattice[0,1] == 1 or lattice[1,0] == 1:
            return True
    elif pos[0] == 0 and pos[1] == col-1: # if particle at north-east
        if lattice[0,col-2] == 1 or lattice[1,col-1] == 1:
            return True
    elif pos[0] == row-1 and pos[1] == col-1: # if particle at south-east
        if lattice[row-2,col-1] == 1 or lattice[row-1,col-2] == 1:
            return True
    elif pos[0] == row-1 and pos[1] == 0: # if particle at south-west
        if lattice[row-2,0] == 1 or lattice[row-1,1] == 1:
            return True
    elif pos[0] == 0: # if particle at north
        if lattice[0,pos[1]-1] == 1 or lattice[0,pos[1]+1] == 1 or lattice[1,pos[1]] == 1:
            return True
    elif pos[1] == col-1: # if particle at east
        if lattice[pos[0]-1,col-1] == 1 or lattice[pos[0]+1,col-1] == 1 or lattice[pos[0],pos[1]-1] == 1:
            return True
    elif pos[0] == row-1: # if particle at south
        if lattice[row-1,pos[1]+1] == 1 or lattice[row-1,pos[1]-1] == 1 or lattice[row-2,pos[1]] == 1:
            return True
    elif pos[1] == 0: # if particle at west
        if lattice[pos[0]-1,0] == 1 or lattice[pos[0]+1,0] == 1 or lattice[pos[0],1] == 1:
            return True
     
    elif lattice[pos[0],pos[1]+1] == 1: # is to the right
        return True
    elif lattice[pos[0],pos[1]-1] == 1: # is to the left
        return True
    elif lattice[pos[0]+1,pos[1]] == 1: # is up
        return True
    elif lattice[pos[0]-1,pos[1]] == 1: # is down
        return True
    
    return False

def update_lattice(lattice,old_pos,new_pos):
    lattice[old_pos[0],old_pos[1]] = 0
    lattice[new_pos[0],new_pos[1]] = 1
    return lattice

def plot_heatmap(lattice):
    #plt.xkcd()
    fig, ax = plt.subplots()
    im = ax.imshow(lattice)

    plt.show()
    #return "not implemented yet"

if __name__ == "__main__":
    pass

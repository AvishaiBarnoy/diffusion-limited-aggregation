import numpy as np
import matplotlib.pyplot as plt
import functions as fn
import argparse
import matplotlib.pyplot as plt

# Pseudo code
# 1. particle starts randomly on edges
#   1.1 def init_particle
# 2. partice diffuses randomly
#   2.1 def take_random_walk
#   2.2 check neighbor
#   2.3 update lattice for new particle position
# 3. repeat n times

# Args:
#   1. lattice size
#   2. number of particles

parser = argparse.ArgumentParser(
                    prog = 'Diffusion-Limited Aggregation Simulation',
                    description = 'runs basic DLA simulation',
                    epilog = 'The End.')
parser.add_argument("-s", "--size",help="lattice size",default=2,type=int)
parser.add_argument("-n", "--nparticles",help="number of particles to deposit",default=2,type=int)
args = parser.parse_args()

print("Running LDA simulation")
print(f"lattice size: {args.size}\nnumber of particles: {args.nparticles}") 
# add here an estimation of a too large ratio of nparticle/lattice_size

if __name__ == "__main__":
    system_size = args.size
    lattice = fn.init_lattice(system_size)
    
    n_particles = args.nparticles
    for i in range(n_particles): # number of particles to deposit
        deposit = False
        new_part = fn.init_particle(lattice)
        lattice[new_part[0],new_part[1]] = 1
        
        part_pos = (new_part[0],new_part[1])

        deposit = fn.check_deposit(lattice,new_part)
        while deposit == False:
            new_pos = fn.choose_direction(lattice,part_pos)
            lattice = fn.update_lattice(lattice,part_pos,new_pos)
            part_pos = new_pos
            deposit = fn.check_deposit(lattice,new_pos)
        
    np.savetxt(f"sim_n{n_particle}_s{system_size}.csv",lattice,fmt="%i",delimiter=',')
    fn.plot_heatmap(lattice)

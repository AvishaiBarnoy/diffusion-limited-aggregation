# Diffusion Limited Aggregation (DLA)
This is my implementation of the DLA algorithm which describes physical growth
of particles that are limited by the diffusion of particles.
The algorithm was developed by TA Witten Jr, LM Sander and described in their paper
[Diffusion Limited Aggregation, a Kinetic Critical Phenomena](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.47.1400)
DLA can be used to describe cloud formation, crystal growth, and maybe most important the shape and structure of Dust Bunnies.

# Algorithm Description
The algorithm is rather simple
1. one particle starts in the middle of the lattice
2. a particle is initiated at the edge and allowed to do a random walk on the lattice
3. when the particle lands in a cell neighboring an occupied one it deposits
4. another partilce is initiated

# About Me
I am a biophysics PhD student and decided to make this simulation after learning about it in a course I took in non-equilibrium statistical mechanics.

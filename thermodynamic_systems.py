from math import comb, log

# importing matplotlib module 
from matplotlib import pyplot as plt 

class system_2l:
    
    def __init__(self, n_particles, energy):
        self.n_particles = n_particles
        self.energy = energy

        
    def energy_per_particle(self):
        print(self.energy/self.n_particles)

    def m_vs_e(self, show_plot=True):
        # Plot microstates as a function of energy
        energies = list(range(0,self.n_particles+1))
        microstates = [comb(self.n_particles,e) \
                       for e in energies]
          
        if show_plot:
            # Function to plot 
            plt.plot(energies, microstates) 
            plt.xlabel('energy')
            plt.ylabel('# microstates')
            plt.grid(True)
            # function to show the plot 
            plt.show()

        return energies, microstates
    
    def s_vs_e(self, show_plot=True, k_b=1):
        # Plot microstates as a function of energy
        energies = list(range(0,self.n_particles+1))
        s = [log(comb(self.n_particles,e)) \
                       for e in energies]
          
        if show_plot:
            # Function to plot 
            plt.plot(energies, s) 
            plt.xlabel('energy')
            plt.ylabel('entropy')
            plt.grid(True)
            # function to show the plot 
            plt.show()

        return energies, s
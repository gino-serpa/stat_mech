from math import comb, log

# importing matplotlib module 
from matplotlib import pyplot as plt 

class system_2l:
    
    def __init__(self, n_particles, energy):
        self.n_particles = n_particles
        self.energy = energy

        
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
        s = [k_b*log(comb(self.n_particles,e)) \
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
    
     
def thermal_eq(system_1, system_2):
    # e_total
    e_t = system_1.energy + system_2.energy
    
    # plot the possible microstates of 1
    energies = list(range(0, e_t+1))
    micro_1 = [comb(system_1.n_particles, e_1)\
               for e_1 in energies]
    micro_2 = [comb(system_2.n_particles, e_t-e_1)\
               for e_1 in energies]
    micro = [m_1 * m_2 for m_1,m_2 in zip(micro_1,micro_2)]

    plt.plot(energies, micro_1)
    plt.plot(energies, micro_2)
    plt.plot(energies, micro)

    plt.show()
    
    return 1/7   
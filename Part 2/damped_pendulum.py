#%%
from pendulum import Pendulum
from operator import xor
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DampenedPendulum(Pendulum):
    def __init__(self, L=1, M=1, B=1, g=9.81):
        self.L = L  # length of pendulum [m]
        self.M = M  # mass of pendulum [kg]
        self.B = B 
        self.g=g    # gravitational acceleration [kg/ms**2]
        self.solution = None
        self.__theta = None
        self.__omega = None
        self.__t = None
        self.__x = None
        self.__y = None
        self.__P = None
        self.__K = None
        self.__vx = None
        self.__vy = None
        self.__dt = None





    def __call__(self, t, y):
        theta, omega = y
        g, L, B, M = self.g, self.L, self.B, self.M

        theta_dot = omega
        omega_dot = (-g/L)*np.sin(theta) - (B/M)*(omega)

        return theta_dot, omega_dot
    
    def create_animation(self):
    # Create empty figure
        fig = plt.figure()

    # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-4, 4, -4, 4))
        
       
        x0 = self.x[0]
        y0 = self.y[0]

        self.pendulums, = plt.plot([0, x0], [0, y0],'o-', lw=3)
        self.animation = animation.FuncAnimation(fig,
                                                self._next_frame,
                                                frames=range(len(self.x)), 
                                                repeat=None,
                                                interval=1000*(1/60), 
                                                blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data([0,self.x[i]], [0,self.y[i]])
        return self.pendulums,



if __name__=="__main__":
    test = DampenedPendulum(2.7,1)
    test.solve((45,0),100,1/60,angle="deg")
    test.create_animation()
    plt.show()

    
# %%

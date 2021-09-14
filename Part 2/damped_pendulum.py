#%%
from pendulum_2 import Pendulum_2
from operator import xor
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


class DampenedPendulum(Pendulum_2):
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

    def __call__(self, t, y):
        theta, omega = y
        g, L, B, M = self.g, self.L, self.B, self.M

        theta_dot = omega
        omega_dot = (-g/L)*np.sin(theta) - (B/M)*(omega)

        return theta_dot, omega_dot
        
    
# %%

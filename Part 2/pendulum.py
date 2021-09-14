#%%
from operator import xor
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


class Pendulum():
    def __init__(self, L, M, g=9.81):
        self.L = L  # length of pendulum [m]
        self.M = M  # mass of pendulum [kg]
        self.g=g    # gravitational acceleration [kg/ms**2]
        self.solution = None
        self.__theta = None
        self.__omega = None
        self.__t = None
        self.__x = None
        self.__y = None
        self.__P = None
        self.__K = None


    @property
    def theta(self):
        if self.__theta is None:
            raise Exception("theta is missing")
        return self.__theta
    @theta.setter
    def theta(self, y):
        self.__theta = y

    @property
    def omega(self):
        if self.__omega is None:
            raise Exception("omega is missing")
        return self.__omega
    @omega.setter
    def omega(self, y):
        self.__omega = y
    
    @property
    def t(self):
        if self.__t is None:
            raise Exception("t is missing")
        return self.__t
    @t.setter
    def t(self, y):
        self.__t = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, y):
        self.__x = y
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def P(self):
        return self.__P
    @P.setter
    def P(self, y):
        self.__P = y
    
    @property
    def K(self):
        return self.__K
    @K.setter
    def K(self, y):
        self.__K = y


    def __call__(self, t, y):
        theta, omega = y
        theta_dot = omega
        omega_dot = (-self.g/self.L)*np.sin(theta)

        return theta_dot, omega_dot

    def solve(self,y0, T, dt,angle="rad"):
        if angle == "deg":
            y0_rad = (np.radians(y0[0]),y0[1])
        elif angle =="rad":
            y0_rad = y0

        interval = np.arange(0,T,dt)
        res = solve_ivp(self, y0=(y0_rad),t_span=[0,T], t_eval=interval)
        self.t = res.t
        self.omega = res.y[0]
        self.theta = res.y[1]
        self.y = self.L*np.sin(self.theta)
        self.x = (-self.L)*np.cos(self.theta)
        




# %%

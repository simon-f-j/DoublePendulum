#%%
from operator import xor
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt




class Pendulum_2():
    def __init__(self, L=1, M=1, g=9.81):
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
        self.__vx = None
        self.__vy = None



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

    @property
    def vx(self):
        return self.__vx
    @vx.setter
    def vx(self, y):
        self.__vx = y

    @property
    def vy(self):
        return self.__vy
    @vy.setter
    def vy(self, y):
        self.__vy = y

    @property
    def kinetic(self):
        v_x = np.gradient(self.vx, 0.1)
        v_y = np.gradient(self.vy, 0.1)
        return 0.5*self.M*(np.power(v_x,2) + np.power(v_y,2))



    
    def __call__(self, t, y):
        theta, omega = y
        g, L = self.g, self.L

        theta_dot = omega
        omega_dot = (-g/L)*np.sin(theta)

        return theta_dot, omega_dot





    def solve(self, y0,T,dt,angle="rad"):
        if angle == "deg":
            y0_rad = (np.radians(y0[0]),y0[1])
        elif angle =="rad":
            y0_rad = y0

        interval = np.arange(0,T,dt)

        self.solution = solve_ivp(self,y0=y0_rad,t_span=[0,T], t_eval=interval)
        self.theta = self.solution.y[0]
        self.omega = self.solution.y[1]
        self.t = self.solution.t[0]

        self.x = self.L*np.sin(self.theta)
        self.y = -self.L*np.cos(self.theta)
        self.t = interval

        # potential energy
        mg = self.M*self.g
        self.P = mg*(self.y+self.L)

        # kinetic energy
        self.vx = np.gradient(test.x, dt)
        self.vy = np.gradient(test.y, dt)

        self.K = 0.5*self.M*(np.power(self.vx,2) + np.power(self.vy,2))





if __name__ =="__main__":
    test = Pendulum_2(2.7)
    print(test(None,(0,0)))
    print(test(None,(np.pi/6,0.15)))
    test.solve((np.pi/2,0),10,0.1)
    
    plt.figure("Theta v Time")
    plt.plot(test.t,test.theta)
    plt.legend("theta")
    plt.xlabel("Time [s]")
    plt.ylabel("Angle [rad]")
    plt.figure("Potential v Kinetic energy")
    plt.plot(test.t,test.P)
    plt.legend("potential energy")
    plt.plot(test.t,test.K)
    plt.legend("kinetic energy")
    plt.xlabel("Time [s]")
    plt.ylabel("Energy [N]")
    # plt.plot(test.t,test.P)
    plt.show()

# %%

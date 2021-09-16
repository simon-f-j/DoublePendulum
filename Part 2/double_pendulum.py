#%%
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt




class DoublePendulum():
    """ A class representing a double pendulum og lengths L1, L2 and masses M1=M2
    """
    def __init__(self, L1=1, L2=1, M=1, g=9.81):
        self.L1 = L1  # length of pendulum 1 [m]
        self.L2 = L2  # length of pendulum 1 [m]
        self.M = M  # mass of pendulum [kg]
        self.g=g    # gravitational acceleration [kg/ms**2]
        self.solution = None
        self.t = None
        self.vx1 = None
        self.vx2 = None
        self.vy1 = None
        self.vy2 = None
        self.__theta1 = None
        self.__theta2 = None
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__P = None
        self.__K = None
        self.__Etotal = None
        self.dt = None


    @property
    def theta1(self):
        if self.__theta1 is None:
            raise Exception("theta_1 is missing")
        return self.__theta1
    @theta1.setter
    def theta1(self, y):
        self.__theta1 = y

    @property
    def theta2(self):
        if self.__theta2 is None:
            raise Exception("theta_2 is missing")
        return self.__theta2
    @theta2.setter
    def theta2(self, y):
        self.__theta2 = y

    @property
    def x1(self):
        if self.__x1 is None:
            raise Exception("x1 is missing")
        return self.__x1
    @x1.setter
    def x1(self, y):
        self.__x1 = y

    @property
    def x2(self):
        if self.__x2 is None:
            raise Exception("x2 is missing")
        return self.__x2
    @x2.setter
    def x2(self, y):
        self.__x2 = y

    @property
    def y1(self):
        if self.__y1 is None:
            raise Exception("y1 is missing")
        return self.__y1
    @y1.setter
    def y1(self, y):
        self.__y1 = y

    @property
    def y2(self):
        if self.__y2 is None:
            raise Exception("y2 is missing")
        return self.__y2
    @y2.setter
    def y2(self, y):
        self.__y2 = y

    @property
    def P(self):
        if self.__P is None:
            raise Exception("P is missing")
        return self.__P
    @P.setter
    def P(self, y):
        self.__P = y

    @property
    def K(self):
        if self.__K is None:
            raise Exception("K is missing")
        return self.__K
    @K.setter
    def K(self, y):
        self.__K = y

    @property
    def Etotal(self):
        if self.__Etotal is None:
            raise Exception("Etotal is missing")
        return self.__Etotal
    @Etotal.setter
    def Etotal(self, y):
        self.__Etotal = y





    def __call__(self, t, y):
        theta1, omega1, theta2, omega2 = y
        L1, L2, g = self.L1, self.L2, self.g
        delta_theta = theta2 - theta1

        theta1_dot = omega1
        theta2_dot = omega2

        eq1_over = (L1 * omega1**2 * np.sin(delta_theta) * np.cos(delta_theta)
                    + g * np.sin(theta2) * np.cos(delta_theta)
                    + L2 * omega2**2 * np.sin(delta_theta)
                    - 2 * g * np.sin(theta1))
        
        eq1_under = (2*L1 - L1*np.cos(delta_theta)**2)

        eq2_over = ((-L2) * omega2**2 * np.sin(delta_theta) * np.cos(delta_theta)
                    + 2 * g * np.sin(theta1) * np.cos(delta_theta)
                    - 2 * L1 * omega1**2 * np.sin(delta_theta)
                    - 2 * g * np.sin(theta2))
        
        eq2_under = 2*L2 - L2*np.cos(delta_theta)**2



        omega1_dot = eq1_over/eq1_under
        omega2_dot = eq2_over/eq2_under

        return theta1_dot, omega1_dot, theta2_dot, omega2_dot

    def solve(self, y0, T, dt, angle="rad"):
        if angle == "deg":
            y0_rad = (np.radians(y0[0]),y0[1],np.radians(y0[2]), y0[3])
        elif angle =="rad":
            y0_rad = y0

        # creating a vector with steplength dt from 0 to T
        interval = np.arange(0,T,dt)

        # solving the equation with initial conditions y0, for the specified vector
        self.solution = solve_ivp(self,y0=y0_rad,t_span=[0,T], t_eval=interval,method="Radau")

        # storing the timesteps
        self.t = self.solution.t
        # storing the variables theta_1 and theta_2 on their respective attributes
        self.theta1 = self.solution.y[0]
        self.theta2 = self.solution.y[2]

        # storing the carthesian coordinates on attributes x and y
        self.x1 = self.L1*np.sin(self.solution.y[0])
        self.y1 = -self.L1*np.cos(self.solution.y[0])       
        self.x2 = self.x1 + self.L2*np.sin(self.solution.y[2])
        self.y2 = self.y1 - self.L2*np.cos(self.solution.y[2])

        # calculating potential and kinetic energy
        P1 = self.M*self.g*(self.y1 + self.L1)
        P2 = self.M*self.g*(self.y2 + self.L1 + self.L2)
        self.P = P1 + P2


        self.vx1 = np.gradient(self.x1, dt)
        self.vy1 = np.gradient(self.y1, dt)
        self.vx2 = np.gradient(self.x2, dt)
        self.vy2 = np.gradient(self.y2, dt)
        
        K1 = 0.5*self.M*(self.vx1**2 + self.vy1**2)
        K2 = 0.5*self.M*(self.vx2**2 + self.vy2**2)
        self.K = K1 + K2

        # calculating total energy
        self.Etotal = self.K + self.P
        

if __name__=="__main__":
    theta1 = 90
    theta2 = 180
    omega1 = 0
    omega2 = 0
    
    y = (theta1, omega1, theta2, omega2)
    test = DoublePendulum()
    test.solve(y,10,0.1)


    #plt.plot(test.t,test.K)
    #plt.plot(test.t,test.P)
    plt.plot(test.t,test.Etotal)
    plt.show()


# %%

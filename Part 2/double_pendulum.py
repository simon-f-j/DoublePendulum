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
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.dt = None

    def __call__(self, t, y):
        theta1, omega1, theta2, omega2 = y
        L1, L2, g = self.L1, self.L2, self.g
        delta_theta = theta2 - theta1

        theta1_dot = omega1
        theta2_dot = omega2

        eq1_over = (L1*omega1**2*np.sin(delta_theta)*np.cos(delta_theta)
                    + g*np.sin(theta2)*np.cos(delta_theta)
                    + L2*omega2**2*np.sin(delta_theta)
                    - 2*g*np.sin(theta1))
        
        eq1_under = 2*L1 - L1*np.cos(delta_theta)**2

        eq2_over = ((-L2)*omega2**2*np.sin(delta_theta)
                    + 2*g*np.sin(theta1)*np.cos(delta_theta)
                    - 2*L1*omega1**2*np.sin(delta_theta)
                    - 2*g*np.sin(theta2))
        
        eq2_under = 2*L2 - L2*np.cos(delta_theta)**2

        omega1_dot = eq1_over/eq1_under
        omega2_dot = eq2_over/eq2_under

        return theta1_dot, omega1_dot, theta2_dot, omega2_dot



        





if __name__=="__main__":
    theta1 = 90
    theta2 = 180
    omega1 = 0
    omega2 = 0
    
    y = (theta1, 0.25, theta2, 0.15)

    test = DoublePendulum()

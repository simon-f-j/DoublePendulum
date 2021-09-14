#%%
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt



class ExponentialDecay():
    """Class for solving exponential decay."""
    def __init__(self, a):
        if a > 0 : self.a = a
        elif a < 0 : raise ValueError('a should be a positive number')

    def __call__(self,t,u):
        dudt = (-self.a)*u
        return dudt
    
    def solve(self, u0, T, dt):
        interval = np.arange(0,T,dt)
        res = solve_ivp(self, y0=[u0],t_span=[0,T], t_eval=interval)
        return res.t, res.y





if __name__ == "__main__":
    test = ExponentialDecay(0.4)
    t, u = test.solve(5,10,0.1)
    plt.plot(t,u[0])
    plt.show()
    print(test.a)


# %%


from scipy.integrate import solve_ivp
from math import exp
from numpy import linspace



class ExponentialDecay():
    def __init__(self, a):
        if a > 0 : self.a = a
        elif a < 0 : raise ValueError('a should be a positive number')

    def __call__(self,t,u):
        dudt = (-self.a)*u
        return dudt
    
    def solve(self, u0, T, dt):
        interval = linspace(dt,T)
        res = solve_ivp(self, y0=[u0],t_span=[0,T], t_eval=interval)
        return res





if __name__ == "__main__":
    test = ExponentialDecay(0.4)
    print(test.a)


#%%
from scipy.integrate._ivp.radau import T
from pendulum import Pendulum
from pendulum_2 import Pendulum_2
import numpy as np
import pytest


def test_Pendulum_call():
    L=2.7
    omega = 0.15
    theta = np.pi/6
    g=9.81

    pend = Pendulum(2.7,1)
    theta_dot,omega_dot = pend(None,(theta,omega))
    
    theta_dot_hand = omega
    omega_dot_hand = ((-g)/L)*np.sin(theta)

    assert theta_dot == theta_dot_hand
    assert omega_dot == omega_dot_hand


def test_Pendulum_call():
    L=2.7
    omega = 0.15
    theta = np.pi/6
    g=9.81

    pend = Pendulum_2(2.7,1)
    theta_dot,omega_dot = pend(None,(theta,omega))
    
    theta_dot_hand = omega
    omega_dot_hand = ((-g)/L)*np.sin(theta)

    assert theta_dot == theta_dot_hand
    assert omega_dot == omega_dot_hand




    

def test_Pendulum_at_rest():
    pend = Pendulum(2.7,1)
    theta = 0
    omega = 0

    theta_dot,omega_dot = pend(None,(theta,omega))
    assert theta_dot == 0
    assert omega_dot == 0


def test_Pendulum_properties():
    pend = Pendulum_2(2.7,1)
    with pytest.raises(Exception):
        pend.theta
        pend.omega
        pend.t


def test_Pendulum_initialcondition():
    pend = Pendulum_2(2.7,1)
    theta_initial = 0
    omega_initial = 0
    T = 10
    dt = 0.1
    interval = np.arange(0,T,dt)
    pend.solve((theta_initial, omega_initial),T,dt)
    
    assert pend.theta.all() == 0
    assert pend.omega.all() == 0
    assert pend.t.all() == interval.all()
        

# %%

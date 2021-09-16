#%%
import pytest
from pytest import approx
from exp_decay import ExponentialDecay
import numpy as np
from math import exp



def test_exp_decay_raisesValueError():
    with pytest.raises(ValueError):
        ExponentialDecay(-0.4)


def test_Expdecay_init():
    ed = ExponentialDecay(0.4)
    assert ed(1,3.2) == approx(-1.28)


def test_Expdecay_solve():
    """
    Testing the exponential decay function
    by solving and comparing the equation with given initial conditions
    """
    u0 = 10
    dt = 0.1
    T = 10
    t = np.arange(0,T,dt)
    a = 0.4

    manual_ans = [u0*exp(-a*timestep) for timestep in t]
    ed = ExponentialDecay(0.4)
    ed_t, ed_y = ed.solve(10,10,0.1)

    for item1,item2 in zip(manual_ans,ed_y[0]):
        assert item1 == approx(item2,0.01)


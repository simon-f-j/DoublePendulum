import pytest
from pytest import approx
from exp_decay import ExponentialDecay

from scipy import integrate
from scipy.integrate import solve_ivp
from math import exp
import matplotlib.pyplot as plt



def test_exp_decay_raisesValueError():
    with pytest.raises(ValueError):
        ExponentialDecay(-0.4)


def test_exp_decay():
    ed = ExponentialDecay(0.4)
    assert ed(1,3.2) == approx(-1.28)

"""
decay_model = ExponentialDecay(1)

sol = solve_ivp(decay_model, [0, 10], [2, 4, 8])
print(sol.t)
plt.plot(sol.t,sol.y[0])
plt.plot(sol.t, sol.y[1])
plt.plot(sol.t, sol.y[2])
plt.show()
"""
from scipy.integrate._ivp.radau import T
from double_pendulum import DoublePendulum
import numpy as np
import pytest



@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (  0,   0,            0),
        (  0, 0.5,  3.386187037), 
        (0.5,   0, -7.678514423),
        (0.5, 0.5, -4.703164534),
    ]
)
def test_domega1_dt(theta1, theta2, expected):
    dp = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    dtheta1_dt, domega1_dt, _, _ = dp(t, y)
    assert np.isclose(dtheta1_dt, 0.25)
    assert np.isclose(domega1_dt, expected)
    
@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (  0,   0,          0.0),
        (  0, 0.5, -7.704787325),
        (0.5,   0,  6.768494455),
        (0.5, 0.5,          0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    dp = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    _, _, dtheta2_dt, domega2_dt = dp(t, y)
    assert np.isclose(dtheta2_dt, 0.15)
    assert np.isclose(domega2_dt, expected)


def test_DoublePendulum_at_origin_with_angular_velocity():
    """Testing that the pendulum moves from angle 0,0 when given an initial speed
    """
    pend = DoublePendulum()
    y = (0, 0.25, 0, 0.15)
    pend.solve(y,10,0.1)

    assert pend.Etotal.all() > 0

def test_DoublePendulum_empty_attribute():
    """Testing for empty attributes
    """
    pend = DoublePendulum()
    with pytest.raises(Exception):
        pend.theta1
        pend.theta2
        pend.vx1
        pend.vx2
        pend.vy1
        pend.vy2
        pend.P
        pend.K
        pend.Etotal
        pend.t

def test_DoublePendulum_no_direct_attribute_access():
    theta1 = 90
    theta2 = 180
    omega1 = 0
    omega2 = 0
    y = (theta1, omega1, theta2, omega2)

    pend = DoublePendulum()
    pend.solve(y,10,0.1)
    with pytest.raises(AttributeError):
        pend.__theta1
        pend.__theta2
        pend.__vx1
        pend.__vx2
        pend.__vy1
        pend.__vy2
        pend.__P
        pend.__K
        pend.__Etotal
        pend.__t



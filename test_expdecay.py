import pytest
from pytest import approx
from exp_decay import ExponentialDecay




def test_exp_decay_raisesValueError():
    with pytest.raises(ValueError):
        ExponentialDecay(-0.4)


def test_exp_decay():
    ed = ExponentialDecay(0.4)
    assert ed(1,3.2) == approx(-1.28)



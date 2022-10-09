from tz2 import minn
from tz2 import mas
import pytest


def test_minn_good():
    assert minn() == min(mas)



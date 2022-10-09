from tz2 import maxx
from tz2 import mas
import pytest



def test_maxx_good():
    assert maxx() == max(mas)



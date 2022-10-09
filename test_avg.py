from tz2 import avg
from tz2 import mas
import pytest
from statistics import mean


def test_avg_good():
    assert avg() == round(mean(mas))


from tz2 import avg
from tz2 import mas2
import pytest
from statistics import mean


def test_avg_good():
    assert avg() == round(mean(mas2))


from tz2 import multt
from tz2 import mas
import pytest


def test_multt_good():
    test_mult = 1
    for i in range(len(mas)):
        b = int(mas[i])
        test_mult = test_mult * b
    #print(test_sum)
    assert multt() == test_mult
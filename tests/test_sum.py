from tz2 import summ
from tz2 import mas
import pytest


def test_summ_good():
    test_sum = 0
    for i in range(len(mas)):
        b = int(mas[i])
        test_sum = test_sum + b
    #print(test_sum)
    assert summ() == test_sum
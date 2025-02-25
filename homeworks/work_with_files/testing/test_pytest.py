import pytest
import functions_pytest as fp
import functions_for_testing as fft


def test_season():
    assert fp.season('snow') == 'winter'
    assert fp.season('sun') == 'summer'
    assert fp.season('qwery') is None


def test_range_list():
    assert 6 in fp.range_list(5, 10)
    assert 150 in fp.range_list(10, 200)
    assert 1500 in fp.range_list(10, 2000)


def test_div():
    assert 1 == fft.div(1, 1)
    assert 10 == fft.div(1200, 120)
    assert 5 != fft.div(24, 5)


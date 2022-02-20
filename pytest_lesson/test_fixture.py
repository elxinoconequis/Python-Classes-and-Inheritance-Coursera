import pytest

# Test functions can directly use fixture names
# as input arguments in which case the fixture instance returned
# from the fixture function will be injected
@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


# '.xfail' (exopect to fail)mark the test function
# as an expected failure if any of the
# conditions evaluate to True
@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == x


@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y


def test_method3(numbers):
    z = 25
    assert numbers[2] == z


# You can also skip test if you put a mark and use the skip command

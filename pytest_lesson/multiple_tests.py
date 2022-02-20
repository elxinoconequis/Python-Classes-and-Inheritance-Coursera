import pytest

# For running multiple files; 2 approaches
# 1) Grouping by substring matching
# 2) Grouping by markers


@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y


@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b


# Use command:
# py.test -k method1 -v
# -k us to represent ?subtstance match -> Run tests by keyword expressions
# -v this flag represents 'verbose', increase verbosity
# no se porque no me funcionó

# peros ifunciona de esta manera:
# pytest multiple_tests.py -k method1
# o bien
# py.test multiple_tests.py -k method2


# Second approach
# We have to specify the markers
# with @
# py.test -m one
# py.test -m two
# m flag indicated marker
# Si ejecuta pytest sin parámetros, primero buscará elementos de configuración de los archivos de configuración

# El siguiente comando si funcionó:
# pytest multiple_tests.py -m "two"

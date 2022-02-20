# import pytest
# ¿Debería siempre importar el m´´odulo pytest?
# Al parecer no es necesario.
class TestClass:
    def test_one(self):
        x = "eureka"
        assert "r" in x

    def test_two(self):
        x = "Hello"
        assert hasattr(x, "check")
        ## hasattr: The hasattr() method returns
        # true if an object has the given named
        # attribute and false if it does not.

import main
import pytest

def test_constructor():
    objeto = main.claseNombre()
    assert objeto.getNombre() == "Pablo"

def test_constructor2():
    objeto = main.claseNombre()
    assert objeto.saludar() == "Juan"

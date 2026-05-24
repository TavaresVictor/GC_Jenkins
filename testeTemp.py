from temperatura import *

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
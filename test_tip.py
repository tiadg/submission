import pytest

from tip import *

def test_pytest():
    assert True == True

# Create your tests below

# Test 1 - check that the function returns the correct value for a 10% tip on a value of 10
def test_10_tip():
	assert calculate_tip(10,10) == 1


# Test 2 - check that the function throws a ValueError error for negative values. Test with -200 (negative 200) as the amount.
def test_value_error():
	with pytest.raises(ValueError):
		calculate_tip(-200,10)


# Test 3 - check that the function throws a TypeError error for string input. Use the string ‘ten’ as input for the tip.
def test_type_error():
	with pytest.raises(TypeError):
		calculate_tip('ten',10)

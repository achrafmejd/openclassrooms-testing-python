from calculate.operators import Operators

module_to_be_tested = Operators()

def test_simple_addition():
    operation = "5 + 1"
    expected_value = 6
    assert module_to_be_tested.addition(operation) == expected_value

def test_simple_multiplication():
    operation = "5 * 1"
    expected_value = 5
    assert module_to_be_tested.multiplication(operation) == expected_value

def test_simple_substraction():
    operation = "5 - 1"
    expected_value = 4
    assert module_to_be_tested.substraction(operation) == expected_value

def test_simple_division():
    operation = "5 / 1"
    expected_value = 5
    assert module_to_be_tested.division(operation) == expected_value

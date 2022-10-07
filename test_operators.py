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

def test_multiple_addition():
    operation = "5 + 8 + 7"
    expected_value = 20
    assert module_to_be_tested.addition(operation) == expected_value

def test_multiple_multiplcation():
    operation = "4*8*2"
    expected_value = 64
    assert module_to_be_tested.multiplication(operation) == expected_value

def test_multiple_substraction():
    operation = "5 - 1 - 2"
    expected_value = 2
    assert module_to_be_tested.substraction(operation) == expected_value

def test_multiple_division():
    operation = "5 / 1 / 2"
    expected_value = 2.5
    assert module_to_be_tested.division(operation) == expected_value

def test_division_by_0():
    operation = "5 / 0"
    expected_value = None
    assert module_to_be_tested.division(operation) == expected_value


def test_multiplcation_by_non_digit():
    operation = "5 * A"
    expected_value = None
    assert module_to_be_tested.multiplication(operation) == expected_value

def test_addition_by_non_digit():
    operation = "5 + A"
    expected_value = None
    assert module_to_be_tested.addition(operation) == expected_value

def test_substraction_by_non_digit():
    operation = "5 - A"
    expected_value = None
    assert module_to_be_tested.substraction(operation) == expected_value

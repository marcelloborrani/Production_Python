# test_math_operations.py
# def add(arg1, arg2):
#     return arg1 + arg2


# def test_add():
#     assert add(10, 20) == 30


from src.math_operations import add, subtract, multiply, divide

def test_add():
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 30

    actual_output = add(input_value_1, input_value_2)

    assert actual_output == expected_output

def test_subtract():
    # Arrange
    input_value_1 = range(1, 100, 1)
    input_value_2 = range(100, 1, -1)
    expected_output = list(range(-99, 99, 2))
    actual_outputs = list()

    # Act
    for input_value_1, input_value_2, expected_output in zip(input_value_1, input_value_2, expected_output):
        actual_output = subtract(input_value_1, input_value_2)
        actual_outputs.append(actual_output)

    # Assert
    assert actual_output == expected_output

def test_multiply():
    # Arrange
    input_value_1 = 5
    input_value_2 = 4
    expected_value = 20

    #Act
    actual_ouput = multiply(input_value_1, input_value_2)

    # Assert
    assert actual_ouput == expected_value

def test_multiply_complex_number_1():
    # Arrang2
    input_value_1 = 2 + 3j
    input_value_2 = 1 + 4j
    expected_value = -10 + 11j

    #Act
    actual_ouput = multiply(input_value_1, input_value_2)

    # Assert
    assert actual_ouput == expected_value

# def test_division_by_zero():
#     # Arrange
#     input_value_1 = 10
#     input_value_2 = 0

#     # Act and Assert
#     try:
#         divide(input_value_1, input_value_2)
#     except ZeroDivisionError:
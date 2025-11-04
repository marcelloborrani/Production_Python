from src.dict_sets import cleanup_address_book, combine_address_books, search_address_book, count_vowels, get_names_in_common, get_numbers_in_common

def test_cleanup_address_book():
    # Arrange
    input_value = {'first last': '1234567890'}
    expected_output = {'First Last': '1234 567890'}

    # Act
    actual_output = cleanup_address_book(input_value)

    # Assert
    assert actual_output == expected_output

def test_search_address_book():
    # Arrange
    input_value_1 = {'first last': '1234567890'}
    input_value_2 = 'fir'
    expected_output = {'first last': '1234567890'}

    # Act
    actual_output = search_address_book(input_value_1, input_value_2)

    # Assert
    assert actual_output == expected_output

def test_count_vowels():
    # Arrange
    input_value_1 = 'hello world'
    expected_output = {'a':0, 'e':1, 'i':0, 'o':2, 'u':0}

    # Act
    actual_output = count_vowels(input_value_1)

    # Assert
    assert actual_output == expected_output

def test_get_names_in_common():
    # Arrange
    input_value_1 = {'John Doe': '1234567890'}
    input_value_2 = {'John Doe': '1234567890'}
    expected_output = {'John Doe'}

    # Act
    actual_output = get_names_in_common(input_value_1, input_value_2)

    # Assert
    # print(actual_output, expected_output)
    assert actual_output == expected_output

def test_get_numbers_in_common():
    # Arrange
    input_value_1 = {'John Doe': '1234567890'}
    input_value_2 = {'John Doe': '1234567890'}
    expected_output = {'1234567890'}

    # Act
    actual_output = get_numbers_in_common(input_value_1, input_value_2)

    # Assert
    # print(actual_output, expected_output)
    assert actual_output == expected_output


def test_combine_address_books():
    # Arrange
    input_value_1 = {'John Doe': '1234567890'}
    input_value_2 = {'Jane Doe': '0987654321'}
    expected_output = ({'John Doe': '1234567890', 'Jane Doe': '0987654321'}, {})

    # Act
    actual_output = combine_address_books(input_value_1, input_value_2)

    # Assert

    print(actual_output, expected_output)

    assert actual_output == expected_output
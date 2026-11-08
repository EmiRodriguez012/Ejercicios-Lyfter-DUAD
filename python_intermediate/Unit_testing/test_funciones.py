from semana_6.ejercicio_3_funciones import sum_of_numbers
from semana_6.ejercicio_4_funciones import reversed_string
from semana_6.ejercicio_5_funciones import uppers_check, lowers_check, main_check
from semana_6.ejercicio_6_funciones import string_organizer
from semana_6.ejercicio_7_funciones import check_for_primes

def test_sum_of_number_returns_sum_of_all_numbers_on_the_list():
    #Arrange
    list_input= [8,6,5,4,5,6,1,2,3]
    #Act
    result= sum_of_numbers(list_input)
    #Assert
    assert result == 40

def test_sum_of_numbers_returns_correct_sum_with_large_numbers():
    # Arrange
    list_input = [1000000, 2000000, 3000000]
    # Act
    result = sum_of_numbers(list_input)
    # Assert
    assert result == 6000000

def test_sum_of_numbers_returns_correct_sum_with_negative_numbers():
    # Arrange
    list_input = [-10, -5, 20, 5]
    # Act
    result = sum_of_numbers(list_input)
    # Assert
    assert result == 10

def test_reversed_string_returns_reversed_strings():
    # Arrange
    input_string = "tuna"
    # Act
    result = reversed_string(input_string)    
    # Assert
    assert result == "anut"

def test_reversed_string_works_with_empty_strings():
    # Arrange
    input_string = ""
    # Act
    result = reversed_string(input_string)    
    # Assert
    assert result == ""

def test_reversed_string_works_with_single_element_strings():
    # Arrange
    input_string = "a"
    # Act
    result = reversed_string(input_string)    
    # Assert
    assert result == "a"

def test_for_upper_check_returns_how_many_upper_case_letters_are_on_a_string():
    # Arrange
    input_uppers ="CAPITAL LETTERS ONLY"
    # Act
    result = uppers_check(input_uppers)
    # Assert
    assert result == 18

def test_for_lowers_check_returns_how_many_lower_case_letters_are_on_a_string():
    # Arrange
    input_lowers ="lower case only"
    # Act
    result = lowers_check(input_lowers)
    # Assert
    assert result == 13

def test_for_main_check_returns_how_many_lower_and_upper_case_letters_are_on_a_string():
    # Arrange
    input_lowers_and_uppers = "Lowers and Uppers COMBINED"
    # Act
    result = main_check(input_lowers_and_uppers)
    # Assert
    assert result == "there are 10 upper letters and 13 lower letters in the text."

def test_for_string_organizer_organizes_strings_into_an_alphabetical_order_list():
    # Arrange
    string_input = "Josue-Mario-Karen-Jack-Oscar"
    # Act
    result = string_organizer(string_input)
    # Assert
    assert result == ["Jack","Josue","Karen","Mario","Oscar"]

def test_for_string_organizer_organizes_strings_into_an_numerical_order_list():
    # Arrange
    string_input = "9-10-250-41-88-3"
    # Act
    result = string_organizer(string_input)
    # Assert
    assert result == [3, 9, 10, 41, 88, 250]

def test_for_string_organizer_organizes_strings_into_an_alphabetical_and_numerical_order_list_mixed_together():
    # Arrange
    string_input = "Josue-3-Mario-9-Karen-10-Jack-41-Oscar-88-250"
    # Act
    result = string_organizer(string_input)
    # Assert
    assert result == [3, 9, 10, 41, 88, 250,"Jack","Josue","Karen","Mario","Oscar"]

def test_check_for_primes_receives_a_list_of_numbers_and_returns_prime_numbers_only():
    # Arrange
    primes_input = [6,9,4,2,6,8,14,50,7,34,67]
    # Act
    result = check_for_primes(primes_input)
    # Assert
    assert result == [2, 7, 67]

def test_check_for_primes_receives_a_list_of_numbers_and_returns_prime_numbers_only():
    # Arrange
    primes_input = [6,9,4,2,6,8,14,50,7,34,67]
    # Act
    result = check_for_primes(primes_input)
    # Assert
    assert result == [2, 7, 67]

def test_check_for_primes_receives_a_list_of_numbers_and_returns_prime_numbers_only_with_empy_list():
    # Arrange
    primes_input = []
    # Act
    result = check_for_primes(primes_input)
    # Assert
    assert result == []

def test_check_for_primes_receives_a_list_of_numbers_and_returns_prime_numbers_only_with_negative_numbers_and_number_1():
    # Arrange
    primes_input = [-5,-9,-6,-8,1,2,3]
    # Act
    result = check_for_primes(primes_input)
    # Assert
    assert result == [2,3]
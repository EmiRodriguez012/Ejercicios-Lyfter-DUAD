import pytest

from python_intermediate.Bubble_sorting_algorthim.regular_bubble_sort import bubble_sort

def test_regular_bubble_sort_runs_with_small_list():
    #Arrange
    list_input = [8,9,5,4,2,7,14,3]
    #Act
    result = bubble_sort(list_input)
    #Assert
    assert result == [2,3,4,5,7,8,9,14]


def test_regular_bubble_sort_runs_with_lists_over_100_numbers():
    #Arrange
    list_input = [
    84, 12, 57, 3, 96, 41, 28, 73, 19, 65,
    8, 102, 34, 51, 7, 89, 23, 110, 46, 15,
    62, 1, 78, 39, 94, 17, 55, 6, 83, 31,
    108, 44, 20, 71, 11, 99, 36, 59, 4, 87,
    26, 114, 49, 14, 68, 32, 91, 5, 76, 22,
    105, 38, 60, 9, 81, 47, 16, 97, 29, 53,
    2, 116, 42, 70, 13, 85, 35, 101, 24, 64,
    10, 92, 48, 18, 79, 30, 112, 56, 21, 67,
    37, 103, 25, 88, 43, 118, 54, 0, 75, 33,
    95, 27, 109, 50, 69, 40, 6, 86, 45, 104,
    63, 113, 52, 77, 31, 98, 58, 115, 72, 90,
    66, 106, 80, 117, 74, 107, 100, 93, 111, 119
]
    #Act
    result = bubble_sort(list_input)
    #Assert
    assert result == sorted(list_input)

def test_regular_bubble_sort_runs_with_empty_list():
    #Arrange
    list_input = []
    #Act
    result = bubble_sort(list_input)
    #Assert
    assert result == []

def test_regular_bubble_sort_runs_with_incorrect_elements_list():
    #Arrange
    list_input = [5,10,9,"hola",6]
    #Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(list_input)
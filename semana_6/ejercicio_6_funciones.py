def string_organizer(string):
    string_list= string.split("-")
    words = []
    numbers = []
    for element in string_list:
        if element.isdigit():
            numbers.append(int(element))
            pass
        else:
            words.append(element)
            pass
    
    sorted_words = sorted(words)
    sorted_numbers = sorted(numbers)
    combined_sorted_list = sorted_numbers + sorted_words
    return combined_sorted_list






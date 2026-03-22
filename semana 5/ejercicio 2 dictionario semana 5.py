first_dictionary = {
    "first_list": [ "How","to","combine" ]
}

second_dictionary = {
    "second_list": [ "two","dictionaries","in" ,"one"]
}

combined_dictionary= {
    "combined_list" : first_dictionary["first_list"] + second_dictionary ["second_list"]
}

print(combined_dictionary)
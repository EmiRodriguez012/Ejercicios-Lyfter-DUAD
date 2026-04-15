def string_organizer(text):
    string_list= text.split("-")
    string_list = sorted(string_list)
    return string_list

string_list= input("Please enter a list of words divided by (-):")

print(string_organizer(string_list))

    
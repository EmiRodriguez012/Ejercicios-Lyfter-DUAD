def reversed_list(string):
    reversed_string = ""
    for letters in range (len (string)-1,-1,-1):
        reversed_string += string[letters]
    return reversed_string

print (reversed_list("Hello world"))
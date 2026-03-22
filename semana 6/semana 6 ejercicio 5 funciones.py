def lowers_check(text):
    lowers = ""
    for letter in text:
        if letter.islower():
            lowers += letter
                  
    return len(lowers)
        


def uppers_check(text):
    uppers= "" 
    for letter in text:
        if letter.isupper():
            uppers += letter
        
    return len(uppers)

def main_check (text):
    lowers= lowers_check(text)
    uppers= uppers_check(text)
    return f"there are {lowers} lower letters and {uppers} capital letters in the text."

          
print(main_check ("The are Five CAPITAL letter and two Lower Letters"))



from menu import menu_options

def main():
    students_list = []
    while True: 
        result = menu_options(students_list)
        
        if result is None:
            break
        
        students_list = result
main()

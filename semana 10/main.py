from menu import menu_opcions

def main():
    students = []
    while True: 
        result = menu_opcions(students)
        
        if result is None:
            break
        
        students = result
main()

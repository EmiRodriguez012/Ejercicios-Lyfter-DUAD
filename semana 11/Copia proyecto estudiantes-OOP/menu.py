from actions import create_student, show_students, show_top3_students, show_students_ponderates_average, save_students_csv, load_students_csv


def show_menu():
    print ("\n---menu---")
    print ("1. Add new student")
    print ("2.Show all students")
    print ("3.Show top 3 students")
    print ("4.Show student ponderates")
    print ("5.Export all data to CSV")
    print ("6.Import all data from CSV")
    print ("7.Exit")

def menu_options(students_list):
    
        show_menu()
        option= input("Please select an option:")

        if option == "1":
            print("Add new student")
            students_list.append(create_student())
        elif option == "2":
            print("Show all students")
            show_students(students_list)
        elif option == "3":
            print("Show top 3 students")
            show_top3_students(students_list)
        elif option == "4":
            print("Show student ponderates")
            show_students_ponderates_average(students_list)
        elif option == "5":
            print ("Export all data to CSV")
            save_students_csv(students_list)
        elif option == "6":
            print ("Import all data from CSV")
            students_list= load_students_csv()
        elif option == "7":
            print ("Exiting program")
            return None
        else:
            print("Invalid opcion, please try again:")
        
        return students_list
            


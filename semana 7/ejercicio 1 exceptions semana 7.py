try: 
    while True:
        try:
            current_number = float(input("Please enter a number to start: \n"))
            break
        except ValueError: 
            print ("Invalid input, please enter a valid number.")

    def sum_number(current_number):
            while True:
                try: 
                    user_number = float(input("Enter a number to sum: \n"))
                    result= (current_number + user_number)
                    return result
                except ValueError: 
                    print("Invalid input, please enter a valid number.")


    def rest_number(current_number):
            while True:
                try:
                    user_number = float(input("Enter a number to rest: \n"))
                    result= (current_number - user_number)
                    return result
                except ValueError:
                    print("Invalid input, please enter a valid number.")

    def multiple_number(current_number):
            while True:
                try:
                    user_number = float(input("Enter a number to multiple : \n"))
                    result= (current_number * user_number)
                    return result
                except ValueError:
                    print("Invalid input, please enter a valid number.")

    def divide_number(current_number):
                while True:
                    try:
                        user_number = float(input("Enter a number to divide: \n"))
                        result= (current_number / user_number)
                        return result
                    except ValueError:
                        print ("Invalid input, please enter a valid number.")
                    except ZeroDivisionError:
                        print ("Error, cannot divide by zero, please enter a valid number.")
    while True:
        try:
            calculator_commander= int(input("Please select one of the following options: \n " 
                "\n-----Menu-----\n"
                "Press (1) to sum.\n" 
                "Press (2) to rest.\n" 
                "Press (3) to multiple.\n" 
                "Press (4) to divide.\n" 
                "Press (5) to delete.\n"
                "Press (6) to exit.\n"))
        except ValueError:
            print ("Invalid option. Please enter a number from 1 to 6.\n")
            continue


        if calculator_commander == 1:
            current_number= sum_number(current_number)

        elif calculator_commander == 2:
            current_number= rest_number(current_number)

        elif calculator_commander == 3:
            current_number= multiple_number(current_number)

        elif calculator_commander == 4:
            current_number= divide_number(current_number)

        elif calculator_commander == 5:
            current_number = 0
            print (current_number)

        elif calculator_commander == 6:
            print ("The calculator was closed")
            break 
        else:
            print("Invalid command. Choose a number between 1 and 6.\n")
            continue
        print(f"\nCurrent number {current_number} \n")

except Exception as error:
        print (f"\nAn unexpected error occurred: {error}")

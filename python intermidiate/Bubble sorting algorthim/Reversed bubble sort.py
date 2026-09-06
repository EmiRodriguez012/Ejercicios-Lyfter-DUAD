def bubble_sort(list_to_sort):
    for round in range(len(list_to_sort)-1):
        changes_made = False
        for index in range (len(list_to_sort)-1, round, -1):
            current_element = list_to_sort [index]
            previous_element = list_to_sort [index - 1]
            
            print (f"Round: {round} Index: {index} current element: {current_element} Previous element: {previous_element}")


            if current_element < previous_element:

                print(f"Current element: {current_element} is lower than previous element: {previous_element} , interchanging places!")

                list_to_sort[index - 1] = current_element
                list_to_sort [index] = previous_element
                changes_made = True

        if not changes_made:
            print (f"No more changes to make after round {round}, list is already sorted!")
            return 


list_to_sort = [4,9,10,1,5,4]

my_bubble_sort = bubble_sort (list_to_sort)

print (my_bubble_sort)
def bubble_sort(list_to_sort): 
    for round in range(0 ,len(list_to_sort)-1): # O(n) que al sumarse el anidado es O(n^2)
        changes_made = False
        for index in range (0, len(list_to_sort)-1 -round): # O(n) 
            current_element = list_to_sort [index] # O(1)
            next_element = list_to_sort [index + 1] # O(1)
            
            print (f"Round: {round} Index: {index} Current element: {current_element} Next element: {next_element}") # O(1)




            if current_element > next_element: 

                print(f"Current element: {current_element} is higher than next element: {next_element} , interchanging places!") # O(1)

                list_to_sort[index + 1] = current_element # O(1)
                list_to_sort [index] = next_element # O(1)
                changes_made = True

        if not changes_made: 
            print (f"No more changes to make after round {round}, list is already sorted!")
            return



list_to_sort = [4,9,10,1,5,4]

my_bubble_sort = bubble_sort (list_to_sort)

print (my_bubble_sort)
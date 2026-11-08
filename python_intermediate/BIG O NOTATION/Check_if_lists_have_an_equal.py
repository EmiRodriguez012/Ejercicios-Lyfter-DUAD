def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:  # o(n) como los ciclos estan anidados seria O(n^2)
        for element_b in list_b: # o(n)
           if element_a == element_b:
              return True	
           
    return False 
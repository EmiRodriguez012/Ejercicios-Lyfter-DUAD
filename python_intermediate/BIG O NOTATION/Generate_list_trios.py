def generate_list_trios(list_a, list_b, list_c):
     result_list = []
     for element_a in list_a: # o(n) entonces como estan anidados seria O(n^3)
        for element_b in list_b: # o(n)
            for element_c in list_c: # o(n)
               result_list.append(f'{element_a} {element_b} {element_c}') 
     return result_list 
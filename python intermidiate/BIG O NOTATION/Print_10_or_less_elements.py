def print_10_or_less_elements(list_to_print):
   list_len =len(list_to_print) # o(1) este seria el de orden de magnitud mayor
   for index in range(min(list_len, 10)): # 0(1) 
     print(list_to_print[index]) # o(1)
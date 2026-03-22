first_list = [
	'first',
	'combining',
	'lists' ,
    'one'  
]
second_list= [
	'time', 
	'two' ,
	'with' ,
	'iteration' 
]

combined_list= [

]

for combined in range(0, max(len(first_list), len(second_list))): 
	if combined < len(first_list):
	    combined_list.append(first_list[combined])
	if combined < len(second_list):
	    combined_list.append(second_list[combined])
	
print(combined_list)
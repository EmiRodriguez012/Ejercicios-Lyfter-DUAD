user_list= [

]
counter = 0 
user_entry= 10

while counter < user_entry:
    counter += 1
    user= int(input(f"Please enter number {counter}: "))
    user_list.append(user)

element = 0
current_higher = user_list[element]

for element in user_list:
    if element > current_higher:
        current_higher = element
    
 
print (f"From the list {user_list}, the highest number is {current_higher}")
numbers = [
   
]


count =  int(input("How many numbers would you like to enter?: "))

for i in range(count):
    num = int(input(f"Please enter number {i+1}: "))
    numbers.append(num)

new_list= [

]


for element in numbers:
    if element % 2 == 0:
        new_list.append(element)



print (new_list)
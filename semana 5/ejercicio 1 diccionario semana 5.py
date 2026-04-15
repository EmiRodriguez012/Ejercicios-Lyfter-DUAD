hotel_dictionary = {
    "rooms" : []
   }


hotel_dictionary ["name"] = input("Please enter the hotel name: ")
hotel_dictionary ["stars"] = int(input("Please enter the amount of stars the hotel has: "))

room_count = int(input("How many rooms would you like to enter:"))

for element in range (room_count):
    print(f"\n       Room{element+1}       ")
    number = (input("Please enter the name: "))
    floor= int(input("Please enter the floor: "))
    price = int(input("Please enter the price: "))

rooms_dictionary= {
    "number": number,
    "floor": floor,
    "price": price, 
}

hotel_dictionary["rooms"].append(rooms_dictionary)

print("\n     Hotel information     ")
print(hotel_dictionary)
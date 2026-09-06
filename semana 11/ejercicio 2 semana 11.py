class Person:
    def __init__(self, name):
        print(f"{name} is on the bus stop!")
        self.name = name

class Bus:

    def __init__(self, max_passengers):
        
        self.max_passengers = max_passengers
        self.bus_list = []
    
    def add_passenger(self, person):
        if len(self.bus_list) >= self.max_passengers:
            print ("The bus is full.")
        else:
            self.bus_list.append(person)
            print(f"{person.name} got on the bus.")

    def remove_passenger(self):
        if self.bus_list:
            person_out= self.bus_list.pop()
            print(f"{person_out.name} left the bus.")
        else:
            print("No persons to remove.")


person_1= Person("Josue")
person_2= Person("Mario")
person_3= Person("Karen")
person_4= Person("Manuela")

bus = Bus(3)

bus.add_passenger(person_1)
bus.add_passenger(person_2)
bus.add_passenger(person_3)
bus.add_passenger(person_4)
bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()
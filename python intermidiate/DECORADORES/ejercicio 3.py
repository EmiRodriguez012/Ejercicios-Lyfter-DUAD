from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        
        
    @property
    def age(self):

        today = date.today()

        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age

def check_for_minor(func):
    def wrapper (user):
        try:
            if user.age < 18:
                raise ValueError ("Person is under age")
                
            return func(user)
            
        except ValueError as e:
            print(f"Error: {e}")
            

    return wrapper


@check_for_minor   
def show_user(user):
    print(f"Person is {user.age} years old.")

user= User(date(2009,5,5))

show_user(user)

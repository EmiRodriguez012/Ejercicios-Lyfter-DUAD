def check_for_numbers(func):

    def wrapper (*args,**kwargs):
        try:

            if not all(isinstance(value, (int, float)) for value in args):
                raise ValueError("Value must be a number")
            
            if not all(isinstance(value, (int, float)) for value in kwargs.values()):
                raise ValueError("Value must be a number")
            
            return func(*args,**kwargs)
        
        except ValueError as e:
            print(f"Error: {e}")
            raise

        
    return wrapper

@check_for_numbers
def show_numbers(*args,**kwargs):

    print(args,kwargs)



show_numbers(10,50,90,5)
show_numbers(5)
show_numbers("josue")



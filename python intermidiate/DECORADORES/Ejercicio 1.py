def check_to_delete_cookies(func):

    def wrapper (cookies):
        
        print(f"amount of cookies: {cookies}")

        if cookies > 10:
            func(cookies)
        else:
            print("It is not necessary to delete cookies at this time.")

        
    return wrapper
    

@check_to_delete_cookies
def delete_cookies(cookies):

    print("Cookies deleted")


delete_cookies(12)
delete_cookies(1)

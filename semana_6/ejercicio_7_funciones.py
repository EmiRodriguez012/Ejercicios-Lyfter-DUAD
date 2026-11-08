

def check_for_primes (numbers):
    primes_list= []
    
    for number in numbers:
        if number > 1:
            for i in range (2, int(number ** 0.5) +1):
                if number % i == 0:
                    break
            else:
                primes_list.append (number)
    return primes_list
            


 
    

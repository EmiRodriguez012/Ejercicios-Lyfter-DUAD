primes_list= []

def primes_check (numbers):
    for number in numbers:
        if number > 1:
            for i in range (2, int(number ** 0.5) +1):
                if number % i == 0:
                    break
            else:
                primes_list.append (number)
    return primes_list
            


 
    
print(primes_check([6,9,4,2,6,8,14,50,7, 34, 12, 67 ]))
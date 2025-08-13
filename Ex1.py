#import this ( lol )

def fizzbuzz_basic():
    """Le basique"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def fizzbuzz_advanced(rules_dict, start=1, end=100):
    """L'avancé
       Je ne savais pas si vous vouliez que la fonction print Fizz, Buzz, et FizzBuzz par défaut. Je suis partis du principe que non..
    """
    # Convert skeys to integers for div
    rules = {int(k): v for k, v in rules_dict.items()}
    
    for i in range(start, end + 1):
        output = ""
        
        #Check Rules
        for divisor in sorted(rules.keys()):
            if i % divisor == 0:
                output += rules[divisor]
        
        # If no rules, print
        print(output if output else i)





# Les test::

print(" \n On s'échauffe : \n")

fizzbuzz_basic()

print("\n La version avancée : \n")

fizzbuzz_advanced({'2': 'hello ', '3': 'world ', '5': ':)'})
def factorial (numero):
    if numero ==0:
        return 1
    elif numero < 0:
        print("El factorial de un número negativo no existe")

    else:
        fact = 1
        
        while(numero > 1): 
            fact *= numero 
            numero -= 1
        return fact 

numero = 5; 

print("El factorial de",numero,"es", factorial(numero)) 

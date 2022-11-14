def factorial(n): 
    
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
    
n = 10; 
print("El factorial",n,"es", factorial(n))
    
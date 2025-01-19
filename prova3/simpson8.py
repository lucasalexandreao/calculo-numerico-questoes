import numpy as np

# Regra de 3/8 de Simpson

def function(x):
    return x

def simpson8(n, a, b, function):
    
    delta = (b-a)/n

    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(0,n+1):
        x = a + delta * i
        if (i == 0 or i == n):
            sum1 += function(x)
            
        elif ((i - 1) % 3 == 0 and i != 1):
            sum3 += 2 * function(x)
            
        else:
            sum2 += 3 * function(x)
            
    return (sum1 + sum2 + sum3) * (3 / 8 * delta)

def main():
    
    a = 1
    b = 2
    n = 100000
        
    approximate_area = simpson8(n, a, b, function)
    
    print(f"A área aproximada é {approximate_area}")
    
if __name__ == "__main__":
    main()
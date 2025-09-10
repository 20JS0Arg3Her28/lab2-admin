"""
Librería de funciones matemáticas básicas
Opción A del laboratorio de CI
"""

import math

def square(n):
    """
    Retorna el cuadrado de un número
    
    Args:
        n (int/float): Número a elevar al cuadrado
        
    Returns:
        int/float: El cuadrado del número
        
    Raises:
        TypeError: Si n no es un número
    """
    if not isinstance(n, (int, float)):
        raise TypeError("El parámetro debe ser un número")
    return n * n

def factorial(n):
    """
    Retorna el factorial de un número entero positivo
    
    Args:
        n (int): Número entero positivo
        
    Returns:
        int: El factorial del número
        
    Raises:
        TypeError: Si n no es un entero
        ValueError: Si n es negativo
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro debe ser un número entero")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """
    Retorna si un número es primo o no
    
    Args:
        n (int): Número a verificar
        
    Returns:
        bool: True si es primo, False si no lo es
        
    Raises:
        TypeError: Si n no es un entero
        ValueError: Si n es menor que 2
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro debe ser un número entero")
    if n < 2:
        raise ValueError("Los números menores a 2 no pueden ser primos")
    
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """
    Retorna el máximo común divisor entre dos números
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor
        
    Raises:
        TypeError: Si a o b no son enteros
        ValueError: Si ambos números son 0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parámetros deben ser números enteros")
    if a == 0 and b == 0:
        raise ValueError("El GCD no está definido cuando ambos números son 0")
    
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Retorna el mínimo común múltiplo entre dos números
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El mínimo común múltiplo
        
    Raises:
        TypeError: Si a o b no son enteros
        ValueError: Si alguno de los números es 0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parámetros deben ser números enteros")
    if a == 0 or b == 0:
        raise ValueError("El LCM no está definido cuando algún número es 0")
    
    return abs(a * b) // gcd(a, b)
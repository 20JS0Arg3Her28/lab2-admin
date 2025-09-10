#!/usr/bin/env python3
"""
Demostración de todas las funciones implementadas
Este script muestra ejemplos de uso de las tres librerías

python3 -m unittest test_math_utils.py -v
"""

from math_utils import square, factorial, is_prime, gcd, lcm

def demo_math_utils():
    """Demostración de funciones matemáticas"""
    print("DEMOSTRACIÓN: MATEMÁTICA BÁSICA")
    print("=" * 50)
    
    # Square
    print(f"square(5) = {square(5)}")
    # print(f"square(5) = {square("test")}")
    print(f"square(-3) = {square(-3)}")
    print(f"square(2.5) = {square(2.5)}")
    
    # Factorial
    print(f"\nfactorial(5) = {factorial(5)}")
    print(f"factorial(0) = {factorial(0)}")
    print(f"factorial(7) = {factorial(7)}")
    
    # Is Prime
    print(f"\nis_prime(17) = {is_prime(17)}")
    print(f"is_prime(15) = {is_prime(15)}")
    print(f"is_prime(2) = {is_prime(2)}")
    
    # GCD
    print(f"\ngcd(48, 18) = {gcd(48, 18)}")
    print(f"gcd(15, 25) = {gcd(15, 25)}")
    print(f"gcd(7, 3) = {gcd(7, 3)}")
    
    # LCM
    print(f"\nlcm(12, 8) = {lcm(12, 8)}")
    print(f"lcm(15, 25) = {lcm(15, 25)}")
    print(f"lcm(7, 3) = {lcm(7, 3)}")


def demo_error_handling():
    """Demostración del manejo de errores"""
    print("\nDEMOSTRACIÓN: MANEJO DE ERRORES")
    print("=" * 50)
    
    error_examples = [
        ("square('text')", lambda: square('text')),
        ("factorial(-1)", lambda: factorial(-1)),
        ("is_prime(1)", lambda: is_prime(1)),
        ("gcd(0, 0)", lambda: gcd(0, 0)),
        ("lcm(0, 5)", lambda: lcm(0, 5)),
    ]
    
    for description, func in error_examples:
        try:
            result = func()
            print(f"{description} = {result} (¡Error! Debería haber fallado)")
        except Exception as e:
            print(f"{description} → {type(e).__name__}: {e}")

if __name__ == '__main__':
    print("DEMOSTRACIÓN COMPLETA DEL LABORATORIO CI")
    print("=" * 70)
    
    demo_math_utils()
    demo_error_handling()
    
    print(f"\n{'='*70}")
    print("¡DEMOSTRACIÓN COMPLETADA!")
    print("Todas las funciones están funcionando correctamente.")
    print("Ejecuta 'python run_tests.py' para verificar las pruebas unitarias.")
    print("="*70)
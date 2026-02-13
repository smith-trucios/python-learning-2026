print("╔══════════════════════════════════╗")
print("║   CALCULADORA SUPER MEJORADA    ║")
print("╚══════════════════════════════════╝")
print()
print("Operaciones disponibles:")
print("  [+]  Suma")
print("  [-]  Resta")
print("  [*]  Multiplicación")
print("  [/]  División")
print("  [**] Potencia")
print("  [%]  Módulo (resto de división)")
print()

# Pide números
try:
    num1 = float(input("Primer número: "))
    operacion = input("Operación: ")
    num2 = float(input("Segundo número: "))
    
    # Calcula según operación
    if operacion == "+":
        resultado = num1 + num2
        print(f"\n✅ {num1} + {num2} = {resultado}")
    
    elif operacion == "-":
        resultado = num1 - num2
        print(f"\n✅ {num1} - {num2} = {resultado}")
    
    elif operacion == "*":
        resultado = num1 * num2
        print(f"\n✅ {num1} × {num2} = {resultado}")
    
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"\n✅ {num1} ÷ {num2} = {resultado}")
        else:
            print("\n❌ ERROR: No se puede dividir por cero")
    
    elif operacion == "**":
        resultado = num1 ** num2
        print(f"\n✅ {num1} elevado a {num2} = {resultado}")
    
    elif operacion == "%":
        if num2 != 0:
            resultado = num1 % num2
            print(f"\n✅ {num1} módulo {num2} = {resultado}")
        else:
            print("\n❌ ERROR: No se puede calcular módulo de cero")
    
    else:
        print(f"\n❌ ERROR: Operación '{operacion}' no válida")

except ValueError:
    print("\n❌ ERROR: Debes ingresar números válidos")

print("\n¡Gracias por usar la calculadora! 👋")
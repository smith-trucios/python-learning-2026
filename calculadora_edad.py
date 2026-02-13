# Calculadora de edad

print("=== CALCULADORA DE TU FUTURO ===")
print()

# Pide información al usuario
nombre = input("¿Cómo te llamas? ")
edad_actual = int(input("¿Cuántos años tienes? "))

# Calcula edades futuras
edad_universidad = edad_actual + (17 - edad_actual)
edad_graduacion = edad_actual + (22 - edad_actual)
edad_senior = edad_actual + (27 - edad_actual)

print("\n=== TU TIMELINE ===")
print(f"Hola {nombre}!")
print(f"Ahora tienes {edad_actual} años")
print(f"A los {edad_universidad} entrarás a la universidad")
print(f"A los {edad_graduacion} te graduarás y ganarás $250K/año")
print(f"A los {edad_senior} serás Senior Engineer ganando $450K+/año")

# Cálculo de ahorros
años_trabajando = int(input("\n¿En cuántos años quieres hacer tu videojuego? "))
salario_promedio = 350000
ahorros = salario_promedio * años_trabajando * 0.4

print(f"\nSi trabajas {años_trabajando} años y ahorras 40% de tu salario:")
print(f"Tendrás ${ahorros:,.0f} para tu videojuego")
print("¡Más que suficiente! 🎮")
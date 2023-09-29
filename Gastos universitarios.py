def calcular_gastos():

    matricula = float(input("Ingrese el costo de la matrícula: "))
    libros = float(input("Ingrese el costo de los libros: "))
    alojamiento = float(input("Ingrese el costo del alojamiento: "))
    comida = float(input("Ingrese el costo de la comida: "))
    transporte = float(input("Ingrese el costo del transporte: "))
    otros = float(input("Ingrese otros gastos (si hay): "))

    total_gastos = matricula + libros + alojamiento + comida + transporte + otros

    print(f"\nEl total de gastos es: ${total_gastos:.2f}")


calcular_gastos()


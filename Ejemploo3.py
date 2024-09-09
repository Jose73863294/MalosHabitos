# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    area = base * altura
    return area

# Función para calcular el área de un triángulo
def area_triángulo(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
def operaciones_matemáticas():
    base = float(input("Base del rectángulo: "))
    altura = float(input("Altura del rectángulo: "))
    area_rectan = area_rectangulo(base, altura)
    print("Área del rectángulo:", area_rectan)

    base = float(input("Base del triángulo: "))
    altura = float(input("Altura del triángulo: "))
    tri_area = area_triángulo(base, altura)
    print("Área del triángulo:", tri_area)

operaciones_matemáticas()

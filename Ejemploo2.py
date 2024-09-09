def ecuación(multiplicando, multipicador, sumando):
    resultado = multiplicando * multipicador + sumando
    return resultado

def principal():
    multiplicando = float(input("Multiplicando: "))
    multipicador = float(input("Multiplicador: "))
    sumando = float(input("Sumando: "))
    resultado = ecuación(multiplicando, multipicador, sumando)
    print("El resultado es:", resultado)

principal()

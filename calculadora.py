class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def converter_celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32


# Exemplo de uso
if __name__ == "__main__":
    calc = Calculadora()

    print("Soma: 5 + 3 =", calc.somar(5, 3))
    print("Subtração: 10 - 4 =", calc.subtrair(10, 4))
    print("Multiplicação: 6 * 7 =", calc.multiplicar(6, 7))
    print("Celsius para Fahrenheit: 25°C =", calc.converter_celsius_para_fahrenheit(25))

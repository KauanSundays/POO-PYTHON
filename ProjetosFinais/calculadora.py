class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def dividir(self):
        return self.a / self.b

    def multiplicar(self):
        return self.a * self.b

# Criar uma instância da classe Calculadora com os valores 5 e 5
c = Calculadora(5, 5)

# Agora você pode acessar os atributos 'a' e 'b na instância 'c' e chamar os métodos
first = c.a
second = c.b

print('O numero {} + {} é igual a: {}'.format(first, second, c.somar()))
print('O numero {} - {} é igual a: {}'.format(first, second, c.subtrair()))
print('O numero {} / {} é igual a: {}'.format(first, second, c.dividir()))
print('O numero {} * {} é igual a: {}'.format(first, second, c.multiplicar()))
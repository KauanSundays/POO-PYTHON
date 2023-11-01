class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Criando uma instância da classe Carro
meuCarro = Carro(marca='gol', modelo='rebaixado', ano=2009)

# A partir deste ponto, você pode acessar os atributos do carro assim:
print("Marca:", meuCarro.marca)
print("Modelo:", meuCarro.modelo)
print("Ano:", meuCarro.ano)

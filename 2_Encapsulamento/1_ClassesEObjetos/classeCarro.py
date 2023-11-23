class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # atributo público
        self.modelo = modelo  # atributo público
        self._ano = ano  # atributo privado

    def obter_ano(self):
        return self._ano


# instanciando
meuCarro = Carro(marca='gol', modelo='rebaixado', ano=2009)

# Acessando o atributo público diretamente
print("Marca:", meuCarro.marca)
print("Modelo:", meuCarro.modelo)

# Acessando o atributo privado através do método de acesso
print("Ano:", meuCarro.obter_ano())

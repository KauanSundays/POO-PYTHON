class MinhaClasse:

    def meu_metodo(self):#Self referencia o contexto que ele esta inserido
        print("Olá, Mundo")
    def outro_metodo(self, num, mult):
        return num * mult
    def __init__(self):
        self.nome = 'kauan' 
        # Declare atributos com o self.

objeto = MinhaClasse()
result = objeto.outro_metodo(5, 2)
att = objeto.nome
print(att)

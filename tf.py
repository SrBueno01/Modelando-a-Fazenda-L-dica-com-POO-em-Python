class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitirSom(self):
        return "o animal emite som."
    
    def saudacao(self):
        print (f"ola, sou {self.nome} e tenho {self.idade} anos")

class cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "AUH AUH"
    
class gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitirSom(self):
        return "MIAUUUUUUU!"

class vaca(Animal):
    def __init__(self, nome, idade, produto_leite):
        super().__init__(nome, idade)
        self._produto_leite = produto_leite

        def emitirSom (self):
            return "MUU"

    def obter_leite(self):
        return self._produto_leite
    
    def ordenha(self, litros):
        self._produto_leite = litros

cachorro = cachorro("cezar" , 2 , "pitbull")
gato = gato("kyev", 6 , "preto")
vaca = vaca("duda" , 8, 25.5)

lista_de_animais = [cachorro, gato, vaca]

for animais in lista_de_animais:
    print(animais.saudacao())
    print(animais.emitirSom ())

print(f"produção atual de leite: {vaca.obter_leite()} litros")

vaca.ordenha(28.0)

print(f"produção de leite após ordenha: {vaca.obter_leite()} litros")
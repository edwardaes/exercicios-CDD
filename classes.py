class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.falando = False

    def comer(self, alimento):
        if self.comendo == False and self.andando == False and self.falando == False:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True
        elif self.andando == True or self.falando == True:
            print(f'{self.nome }, pare para poder comer')
        else:
            print("já está comendo")
    def andar (self):
        if self.comendo == False and self.andando == False and self.falando == False:
            print(f'{self.nome} está andando')
            self.andando = True
        elif self.comendo == True or self.falando == True:
            print(f'{self.nome}, pare para poder andar')
        else:
            print("já está andando")


    def falar (self):
        if self.comendo == False and self.andando == False and self.falando == False:
            print(f'{self.nome} está falando')
            self.falando= True
        elif self.comendo == True or self.andando == True:
            print(f'{self.nome}, pare para poder falar')
        else:
            print("já está falando")

    def pararDeComer(self):
       if self.comendo == True:
           self.comendo = False
           print('parou de comer')
       else:
           print(f'{self.nome} já está sem comer')

    def pararDeAndar(self):
       if self.andando == True:
           self.andando = False
           print('parou de andar')
       else:
           print(f'{self.nome} já está sem andar')

    def pararDeFalar(self):
       if self.falando == True:
           self.falando = False
           print('parou de falar')
       else:
           print(f'{self.nome} já está sem falar')


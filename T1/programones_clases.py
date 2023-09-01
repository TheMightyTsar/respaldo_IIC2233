import abc as abstract
import parametros

'''
Clases relacionadas al funcionamiento de programones
Programon sera una clase abstracta, de la cual heredaran las clases Fuego, Planta y Agua
'''


class Progamon(abstract.ABC):
    def __init__(self, lista, maestro):

        self.maestro = maestro

        self.nombre = lista[0]
        self.tipo = lista[1]
        self._nivel = int(lista[2])
        self._experiencia = 0

        self._vida = int(lista[3])
        self._ataque = int(lista[4])
        self._defensa = int(lista[5])
        self._velocidad = int(lista[6])

    def combate(self, enemy):

        bono_tipo = (parametros.COMBATE_TIPOS[self.tipo])[enemy.tipo]
        puntaje_victoria = bono_tipo * 40
        puntaje_victoria += self.vida * 0.2
        puntaje_victoria += self._nivel * 0.3
        puntaje_victoria += self.ataque * 0.15
        puntaje_victoria += self.defensa * 0.15
        puntaje_victoria += self.velocidad * 0.2

        return puntaje_victoria

    def recibir_objeto(self, objeto):
        print(f"Programon beneficiado: {self.nombre}")
        print(f"Objeto utilizado: {objeto.nombre} (Tipo {objeto.tipo})")
        if objeto.tipo == "baya":
            self.vida += objeto.bonusHP
        elif objeto.tipo == "pocion":
            self.ataque += objeto.bonusAD
        else:
            self.vida += objeto.bonusHP
            self.ataque += objeto.bonusAD
            self.defensa += objeto.bonusDEF

        pass

    @abstract.abstractmethod
    def bonus_tipo(self):
        pass

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, value):
        if self._nivel < parametros.MAX_LVL:
            if value >= parametros.MAX_EXP:
                self._nivel += 1
                self.experiencia += (value - parametros.MAX_LVL)
                print(f"{self.maestro} GUAU tu programon {self.nombre} ha subido un nivel")
                if self._nivel <= parametros.MAX_LVL:
                    self.vida += parametros.AUMENTO_ENTRENAMIENTO
                    self.ataque += parametros.AUMENTO_ENTRENAMIENTO
                    self.defensa += parametros.AUMENTO_ENTRENAMIENTO
                    self.velocidad += parametros.AUMENTO_ENTRENAMIENTO
                    self._experiencia = (value - parametros.MAX_EXP)
                else:
                    print(f"{self.maestro} GUAU tu programon {self.nombre} ya ha llegado a su maximo nivel")
                    self._experiencia = 0
            else:
                print(f"GUAU tu programon {self.nombre} ahora tiene {value} de EXP!")
                self._experiencia = value

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        vida_ganada = value - self._vida
        print(f"{self.maestro} tu programon {self.nombre} tiene un HP de {self._vida}")
        if value < parametros.MAX_VIDA:
            print(f"*HP NOISES*!!! tu programon {self.nombre} ha ganado {vida_ganada} de HP!!! \n "
                  f"ahora tiene {value} de HP")
            self._vida = value
        else:
            print(f"...F... tu programon no puede obtener mas HP")
            self._vida = parametros.MAX_VIDA

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, value):
        ganada = value - self._ataque
        print(f"{self.maestro} tu programon {self.nombre} tiene un Ataque de {self._ataque}")

        if self._ataque == parametros.MAX_ATAQUE:
            print(f"...F... tu programon no puede obtener mas Ataque")
            self._ataque = parametros.MAX_ATAQUE

        elif value < parametros.MAX_ATAQUE:
            print(f"BOOOM!!!! tu programon {self.nombre} ha ganado {ganada} de Ataque!!! \n "
                  f"ahora tiene {value} de Ataque")
            self._ataque = value
            if self._ataque == parametros.MAX_ATAQUE:
                print("Tu programon ha obtenido el maximo de Ataque")



        else:
            ganada = parametros.MAX_ATAQUE - self._ataque
            print(f"BOOOM!!!! tu programon {self.nombre} ha ganado {ganada} de Ataque!!! \n "
                  f"ahora tiene {parametros.MAX_ATAQUE} de Ataque")
            self._ataque = parametros.MAX_ATAQUE


    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, value):
        ganada = value - self._defensa
        print(f"{self.maestro} tu programon {self.nombre} tiene una Defensa de {self._defensa}")

        if value > parametros.MAX_DEFENSA:
            ganada = parametros.MAX_DEFENSA - self._defensa

        if self._defensa == parametros.MAX_DEFENSA:
            print(f"...F... tu programon no puede obtener mas Defensas")
            self._defensa = parametros.MAX_DEFENSA

        else:
            print(f"*ARMOR NOISES*!!! tu programon {self.nombre} ha ganado {ganada} de Defensa!!! \n "
                  f"ahora tiene {self._defensa + ganada} de Defensa")
            self._defensa = self._defensa + ganada
            if self._defensa == parametros.MAX_DEFENSA:
                print("Tu programon ha obtenido el maximo de Defensa")

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, value):
        ganada = value - self.velocidad
        print(f"{self.maestro} tu programon {self.nombre} tiene una Velocidad de {self._velocidad}")

        if value > parametros.MAX_VELOCIDAD:
            ganada = parametros.MAX_VELOCIDAD - self._velocidad

        if self._velocidad == parametros.MAX_VELOCIDAD:
            print(f"...F... tu programon no puede obtener mas velocidad")
            self._velocidad = parametros.MAX_VELOCIDAD

        else:
            print(f"FIUM!!! tu programon {self.nombre} ha ganado {ganada} de Velocidad!!! \n "
                  f"ahora tiene {self._velocidad + ganada} de Velocidad")
            self._velocidad += ganada
            if self._velocidad == parametros.MAX_VELOCIDAD:
                print("Tu programon ha obtenido el maximo de Velocidad")


class Fuego(Progamon):

    def bonus_tipo(self):
        self.ataque += parametros.AUMENTAR_ATAQUE_FUEGO


class Planta(Progamon):

    def bonus_tipo(self):
        self.vida += parametros.AUMENTAR_VIDA_PLANTA


class Agua(Progamon):

    def bonus_tipo(self):
        self.velocidad += parametros.AUMENTAR_VELOCIDAD_AGUA

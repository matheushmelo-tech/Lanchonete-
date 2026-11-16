import math

from produto import Produto


class Bebida(Produto):

    def __init__(self, nome, preco, tamanho_ml, gelada=True):
        super().__init__(nome, preco)
        self.tamanho_ml = tamanho_ml
        self.gelada = gelada

    @property
    def tamanho_ml(self):

        return self.__tamanho_ml

    @tamanho_ml.setter
    def tamanho_ml(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor <= 0
            or not float(valor).is_integer()
        ):
            raise ValueError("O tamanho da bebida deve ser um número inteiro maior que zero.")
        self.__tamanho_ml = int(valor)

    @property
    def gelada(self):

        return self.__gelada

    @gelada.setter
    def gelada(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("O valor de 'gelada' deve ser True ou False.")
        self.__gelada = valor

    def calcular_preco_final(self):
        if self.__tamanho_ml <= 300:
            return self.preco
        if self.__tamanho_ml <= 500:
            return self.preco * 1.20
        return self.preco * 1.40

    def descrever_temperatura(self):
        return "gelada" if self.__gelada else "natural"

    def __str__(self):

        return (
            f"Bebida: {self.nome} | "
            f"Tamanho: {self.__tamanho_ml} ml | "
            f"Servida {self.descrever_temperatura()} | "
            f"Preço base: R$ {self.preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )

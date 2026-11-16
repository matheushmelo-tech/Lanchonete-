import math


class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    @property
    def nome(self):

        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):

        return self.__preco

    @preco.setter
    def preco(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor <= 0
        ):
            raise ValueError("O preço do produto deve ser maior que zero.")
        self.__preco = float(valor)

    def calcular_preco_final(self):
        return self.__preco

    def __str__(self):

        return (
            f"Produto: {self.__nome} | "
            f"Preço base: R$ {self.__preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )

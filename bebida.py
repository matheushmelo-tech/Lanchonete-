"""Módulo que define a classe Bebida, filha de Produto."""

from produto import Produto


class Bebida(Produto):
    """Representa uma bebida vendida pela lanchonete.

    Herda de Produto e adiciona o tamanho (em ml) e se é gelada.
    O preço final varia conforme o tamanho da bebida.
    """

    def __init__(self, nome, preco, tamanho_ml, gelada=True):
        """Inicializa uma bebida.

        Args:
            nome (str): nome da bebida.
            preco (float): preço base (referente a 300 ml).
            tamanho_ml (int): tamanho da bebida em mililitros (maior que zero).
            gelada (bool): indica se a bebida é servida gelada.

        Raises:
            ValueError: se o tamanho for menor ou igual a zero.
        """
        super().__init__(nome, preco)
        self.tamanho_ml = tamanho_ml
        self.gelada = gelada

    @property
    def tamanho_ml(self):
        """int: retorna o tamanho da bebida em mililitros."""
        return self.__tamanho_ml

    @tamanho_ml.setter
    def tamanho_ml(self, valor):
        """Define o tamanho da bebida, impedindo valores inválidos.

        Raises:
            ValueError: se o tamanho não for um número maior que zero.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O tamanho da bebida deve ser maior que zero.")
        self.__tamanho_ml = int(valor)

    @property
    def gelada(self):
        """bool: retorna True se a bebida é servida gelada."""
        return self.__gelada

    @gelada.setter
    def gelada(self, valor):
        """Define se a bebida é gelada.

        Raises:
            ValueError: se o valor não for booleano.
        """
        if not isinstance(valor, bool):
            raise ValueError("O valor de 'gelada' deve ser True ou False.")
        self.__gelada = valor

    def calcular_preco_final(self):
        """Calcula o preço final da bebida de acordo com o tamanho.

        Regra: até 300 ml mantém o preço base; de 301 a 500 ml acrescenta
        20%; acima de 500 ml acrescenta 40%.

        Returns:
            float: preço final da bebida.
        """
        if self.__tamanho_ml <= 300:
            return self.preco
        if self.__tamanho_ml <= 500:
            return self.preco * 1.20
        return self.preco * 1.40

    def descrever_temperatura(self):
        """Retorna um texto indicando como a bebida é servida.

        Returns:
            str: 'gelada' ou 'natural'.
        """
        return "gelada" if self.__gelada else "natural"

    def __str__(self):
        """Retorna os dados da bebida de forma legível."""
        return (
            f"Bebida: {self.nome} | "
            f"Tamanho: {self.__tamanho_ml} ml | "
            f"Servida {self.descrever_temperatura()} | "
            f"Preço base: R$ {self.preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )
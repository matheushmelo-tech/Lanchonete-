"""Módulo que define a classe base Produto da lanchonete (delivery)."""


class Produto:
    """Classe base que representa um produto vendido pela lanchonete.

    As classes filhas (Lanche, Bebida, Sobremesa) herdam desta classe
    e sobrescrevem o método calcular_preco_final().
    """

    def __init__(self, nome, preco):
        """Inicializa um produto.

        Args:
            nome (str): nome do produto (não pode ser vazio).
            preco (float): preço base do produto (deve ser maior que zero).

        Raises:
            ValueError: se o nome for vazio ou o preço for menor ou igual a zero.
        """
        # Usa os setters para que a validação também ocorra na criação do objeto
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        """str: retorna o nome do produto."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome do produto, impedindo valores vazios.

        Raises:
            ValueError: se o nome for vazio ou conter apenas espaços.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        """float: retorna o preço base do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """Define o preço do produto, impedindo valores inválidos.

        Raises:
            ValueError: se o preço não for um número maior que zero.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        self.__preco = float(valor)

    def calcular_preco_final(self):
        """Calcula o preço final do produto.

        Método polimórfico: deve ser sobrescrito pelas classes filhas,
        cada uma com sua própria regra de cálculo.

        Returns:
            float: preço final do produto (na classe base, o próprio preço).
        """
        return self.__preco

    def __str__(self):
        """Retorna os dados do produto de forma legível."""
        return (
            f"Produto: {self.__nome} | "
            f"Preço base: R$ {self.__preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )
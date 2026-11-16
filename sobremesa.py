"""Módulo da classe base Produto da lanchonete."""


class Produto:
    """Representa um produto genérico vendido na lanchonete."""

    def __init__(self, nome, preco):
        """Cria um produto.

        Args:
            nome (str): nome do produto (não pode ser vazio).
            preco (float): preço do produto (deve ser maior que zero).
        """
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        """Retorna o nome do produto."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome do produto, recusando valores vazios."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """Define o preço do produto, recusando valores menores ou iguais a zero."""
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = float(valor)

    def calcular_preco_final(self):
        """Calcula o preço final do produto.

        Método polimórfico: cada classe filha sobrescreve com sua regra.

        Returns:
            float: preço final a ser cobrado.
        """
        return self.preco

    def __str__(self):
        """Retorna os dados do produto de forma legível."""
        return f"{self.nome} - R$ {self.preco:.2f}"
"""Módulo que define a classe Lanche, filha de Produto."""

from produto import Produto


class Lanche(Produto):
    """Representa um lanche/sanduíche vendido pela lanchonete.

    Herda nome e preço de Produto e adiciona o tipo de pão e a lista de
    ingredientes. Sobrescreve calcular_preco_final() cobrando um valor por
    ingrediente acima do limite incluso no preço base.
    """

    INGREDIENTES_INCLUSOS = 3
    VALOR_INGREDIENTE_EXTRA = 2.00

    def __init__(self, nome, preco, pao, ingredientes=None):
        """Inicializa um lanche.

        Args:
            nome (str): nome do lanche.
            preco (float): preço base do lanche (maior que zero).
            pao (str): tipo de pão (ex: 'Brioche', 'Australiano').
            ingredientes (list[str], optional): ingredientes iniciais.

        Raises:
            ValueError: se o pão ou algum ingrediente for vazio.
        """
        super().__init__(nome, preco)
        self.pao = pao
        self.__ingredientes = []
        for ingrediente in ingredientes or []:
            self.adicionar_ingrediente(ingrediente)

    @property
    def pao(self):
        """str: retorna o tipo de pão do lanche."""
        return self.__pao

    @pao.setter
    def pao(self, valor):
        """Define o tipo de pão, impedindo valores vazios.

        Raises:
            ValueError: se o valor for vazio ou conter apenas espaços.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O tipo de pão não pode ser vazio.")
        self.__pao = valor.strip()

    @property
    def ingredientes(self):
        """list: retorna uma cópia da lista de ingredientes do lanche."""
        return self.__ingredientes.copy()

    def adicionar_ingrediente(self, ingrediente):
        """Adiciona um ingrediente ao lanche (método próprio de Lanche).

        Args:
            ingrediente (str): nome do ingrediente.

        Raises:
            ValueError: se o nome do ingrediente for vazio.
        """
        if not isinstance(ingrediente, str) or not ingrediente.strip():
            raise ValueError("O nome do ingrediente não pode ser vazio.")
        self.__ingredientes.append(ingrediente.strip())

    def preparar(self):
        """Descreve o preparo do lanche na cozinha.

        Returns:
            str: texto com o pão e os ingredientes usados.
        """
        ingredientes = ", ".join(self.__ingredientes) or "sem recheio adicional"
        return (
            f"[COZINHA - LANCHE] Selando o pão {self.__pao} "
            f"e montando os ingredientes: {ingredientes}."
        )

    def calcular_preco_final(self):
        """Calcula o preço final do lanche.

        Regra: os primeiros 3 ingredientes já estão no preço base; cada
        ingrediente acima disso acrescenta R$ 2,00.

        Returns:
            float: preço final do lanche.
        """
        extras = max(0, len(self.__ingredientes) - self.INGREDIENTES_INCLUSOS)
        return self.preco + extras * self.VALOR_INGREDIENTE_EXTRA

    def __str__(self):
        """Retorna os dados do lanche de forma legível."""
        ingredientes = ", ".join(self.__ingredientes) or "Receita padrão"
        return (
            f"Lanche: {self.nome} | "
            f"Pão: {self.__pao} | "
            f"Ingredientes: {ingredientes} | "
            f"Preço base: R$ {self.preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )

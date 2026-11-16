

from produto import Produto


class Lanche(Produto):

    INGREDIENTES_INCLUSOS = 3
    VALOR_INGREDIENTE_EXTRA = 2.00

    def __init__(self, nome, preco, pao, ingredientes=None):
        super().__init__(nome, preco)
        self.pao = pao
        self.__ingredientes = []
        for ingrediente in ingredientes or []:
            self.adicionar_ingrediente(ingrediente)

    @property
    def pao(self):

        return self.__pao

    @pao.setter
    def pao(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O tipo de pão não pode ser vazio.")
        self.__pao = valor.strip()

    @property
    def ingredientes(self):

        return self.__ingredientes.copy()

    def adicionar_ingrediente(self, ingrediente):
        if not isinstance(ingrediente, str) or not ingrediente.strip():
            raise ValueError("O nome do ingrediente não pode ser vazio.")
        self.__ingredientes.append(ingrediente.strip())

    def preparar(self):
        ingredientes = ", ".join(self.__ingredientes) or "sem recheio adicional"
        return (
            f"[COZINHA - LANCHE] Selando o pão {self.__pao} "
            f"e montando os ingredientes: {ingredientes}."
        )

    def calcular_preco_final(self):
        extras = max(0, len(self.__ingredientes) - self.INGREDIENTES_INCLUSOS)
        return self.preco + extras * self.VALOR_INGREDIENTE_EXTRA

    def __str__(self):

        ingredientes = ", ".join(self.__ingredientes) or "Receita padrão"
        return (
            f"Lanche: {self.nome} | "
            f"Pão: {self.__pao} | "
            f"Ingredientes: {ingredientes} | "
            f"Preço base: R$ {self.preco:.2f} | "
            f"Preço final: R$ {self.calcular_preco_final():.2f}"
        )

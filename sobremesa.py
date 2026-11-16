"""Módulo que define a classe Sobremesa da lanchonete (delivery)."""

from produto import Produto


class Sobremesa(Produto):
    """Representa uma sobremesa vendida pela lanchonete.

    Herda nome e preço de Produto e adiciona as calorias e a informação
    se a sobremesa é servida gelada. Sobrescreve calcular_preco_final().
    """

    TAXA_EMBALAGEM_TERMICA = 1.50

    def __init__(self, nome, preco, calorias, serve_gelada=False):
        """Inicializa uma sobremesa.

        Args:
            nome (str): nome da sobremesa (não pode ser vazio).
            preco (float): preço base da sobremesa (deve ser maior que zero).
            calorias (int): quantidade de calorias (não pode ser negativa).
            serve_gelada (bool): True se a sobremesa é servida gelada.

        Raises:
            ValueError: se algum dos valores informados for inválido.
        """
        super().__init__(nome, preco)
        # Usa os setters para que a validação também ocorra na criação do objeto
        self.calorias = calorias
        self.serve_gelada = serve_gelada

    @property
    def calorias(self):
        """int: retorna as calorias da sobremesa."""
        return self.__calorias

    @calorias.setter
    def calorias(self, valor):
        """Define as calorias da sobremesa, impedindo valores inválidos.

        Raises:
            ValueError: se o valor não for um número maior ou igual a zero.
        """
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("As calorias não podem ser negativas.")
        self.__calorias = int(valor)

    @property
    def serve_gelada(self):
        """bool: retorna True se a sobremesa é servida gelada."""
        return self.__serve_gelada

    @serve_gelada.setter
    def serve_gelada(self, valor):
        """Define se a sobremesa é servida gelada.

        Raises:
            ValueError: se o valor não for True ou False.
        """
        if not isinstance(valor, bool):
            raise ValueError("serve_gelada deve ser True ou False.")
        self.__serve_gelada = valor

    def calcular_preco_final(self):
        """Calcula o preço final da sobremesa (método sobrescrito).

        Sobremesas geladas recebem uma taxa de embalagem térmica.

        Returns:
            float: preço base, acrescido da taxa se a sobremesa for gelada.
        """
        if self.serve_gelada:
            return self.preco + self.TAXA_EMBALAGEM_TERMICA
        return self.preco

    def descrever_servico(self):
        """Informa como a sobremesa deve ser servida (método próprio).

        Returns:
            str: instrução de serviço da sobremesa.
        """
        if self.serve_gelada:
            return f"{self.nome} deve ser servida gelada, em embalagem térmica."
        return f"{self.nome} deve ser servida em temperatura ambiente."

    def __str__(self):
        """Retorna os dados da sobremesa de forma legível."""
        gelada = "Sim" if self.serve_gelada else "Não"
        return (
            f"[Sobremesa] {super().__str__()} | "
            f"Calorias: {self.__calorias} kcal | "
            f"Gelada: {gelada}"
        )


if __name__ == "__main__":
    # Teste rápido da classe (não executa quando importada pelo main.py)
    pudim = Sobremesa("Pudim", 8.00, 250, serve_gelada=True)
    print(pudim)
    print(pudim.descrever_servico())
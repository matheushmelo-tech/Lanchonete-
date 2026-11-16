

from produto import Produto


class Sobremesa(Produto):

    TAXA_EMBALAGEM_TERMICA = 1.50

    def __init__(self, nome, preco, serve_gelada):
        super().__init__(nome, preco)
        self.serve_gelada = serve_gelada

    @property
    def serve_gelada(self):

        return self.__serve_gelada

    @serve_gelada.setter
    def serve_gelada(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("serve_gelada deve ser True ou False.")
        self.__serve_gelada = valor

    def calcular_preco_final(self):
        if self.serve_gelada:
            return self.preco + self.TAXA_EMBALAGEM_TERMICA
        return self.preco

    def descrever_servico(self):
        if self.serve_gelada:
            return f"{self.nome} deve ser servida gelada, em embalagem térmica."
        return f"{self.nome} deve ser servida em temperatura ambiente."

    def __str__(self):

        gelada = "Sim" if self.serve_gelada else "Não"
        return (
            f"[Sobremesa] {super().__str__()} | "
            f"Gelada: {gelada}"
        )


if __name__ == "__main__":
    pudim = Sobremesa("Pudim", 8.00, serve_gelada=True)
    print(pudim)
    print(pudim.descrever_servico())

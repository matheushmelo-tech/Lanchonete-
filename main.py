
import math

from bebida import Bebida
from lanche import Lanche
from produto import Produto
from sobremesa import Sobremesa


class Lanchonete:

    def __init__(self, nome="Lanchonete"):

        self.nome = nome
        self.__produtos = []

    @property
    def nome(self):

        return self.__nome

    @nome.setter
    def nome(self, valor):

        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome da lanchonete não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def produtos(self):

        return self.__produtos.copy()

    def adicionar_produto(self, produto):

        if not isinstance(produto, Produto):
            raise TypeError("Só é possível cadastrar objetos do tipo Produto.")
        self.__produtos.append(produto)

    def buscar_por_nome(self, termo):

        termo = termo.strip().lower()
        if not termo:
            return []
        return [p for p in self.__produtos if termo in p.nome.lower()]

    def __len__(self):

        return len(self.__produtos)

    def __str__(self):

        return f"Lanchonete: {self.__nome} | Produtos cadastrados: {len(self.__produtos)}"


def ler_texto(mensagem):
    return input(mensagem).strip()


def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem).strip().replace(",", "."))
            if not math.isfinite(numero):
                raise ValueError
            return numero
        except ValueError:
            print("Valor inválido. Digite um número (ex: 12.50).")


def ler_sim_nao(mensagem):
    while True:
        resposta = ler_texto(mensagem).casefold()
        if resposta in {"s", "sim"}:
            return True
        if resposta in {"n", "não", "nao"}:
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def exibir_menu():

    print("\n===== LANCHONETE DELIVERY =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto por nome")
    print("4 - Calcular preço final (polimorfismo)")
    print("0 - Sair")


def criar_lanche():
    nome = ler_texto("Nome do lanche: ")
    preco = ler_numero("Preço (R$): ")
    pao = ler_texto("Tipo de pão: ")
    texto = ler_texto("Ingredientes (separados por vírgula, opcional): ")
    ingredientes = [i.strip() for i in texto.split(",") if i.strip()]
    return Lanche(nome, preco, pao, ingredientes)


def criar_bebida():
    nome = ler_texto("Nome da bebida: ")
    preco = ler_numero("Preço base (R$): ")
    tamanho_ml = ler_numero("Tamanho (ml): ")
    gelada = ler_sim_nao("É gelada? (s/n): ")
    return Bebida(nome, preco, tamanho_ml, gelada)


def criar_sobremesa():
    nome = ler_texto("Nome da sobremesa: ")
    preco = ler_numero("Preco (R$): ")
    serve_gelada = ler_sim_nao("Deve ser servida gelada? (s/n): ")
    return Sobremesa(nome, preco, serve_gelada)

def cadastrar_produto(lanchonete):
    print("\nTipo de produto: 1 - Lanche | 2 - Bebida | 3 - Sobremesa")
    tipos = {"1": criar_lanche, "2": criar_bebida, "3": criar_sobremesa}
    criador = tipos.get(ler_texto("Escolha o tipo: "))
    if criador is None:
        print("Tipo inválido.")
        return
    try:
        produto = criador()
        lanchonete.adicionar_produto(produto)
        print(f"\nProduto cadastrado com sucesso!\n{produto}")
    except ValueError as erro:
        print(f"\nNão foi possível cadastrar: {erro}")


def listar_produtos(lanchonete):
    print(f"\n--- {lanchonete} ---")
    if len(lanchonete) == 0:
        print("Nenhum produto cadastrado.")
        return
    for numero, produto in enumerate(lanchonete.produtos, start=1):
        print(f"{numero}. {produto}")


def buscar_produto(lanchonete):
    termo = ler_texto("\nNome (ou parte do nome) a buscar: ")
    encontrados = lanchonete.buscar_por_nome(termo)
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
    print(f"\n{len(encontrados)} produto(s) encontrado(s):")
    for produto in encontrados:
        print(f"- {produto}")


def executar_polimorfismo(lanchonete):
    if len(lanchonete) == 0:
        print("\nNenhum produto cadastrado.")
        return
    print("\n--- Preço final de cada produto ---")
    for produto in lanchonete.produtos:
        tipo = type(produto).__name__
        print(f"[{tipo}] {produto.nome}: R$ {produto.calcular_preco_final():.2f}")


def main():

    lanchonete = Lanchonete("Lanchonete Delivery")
    acoes = {
        "1": cadastrar_produto,
        "2": listar_produtos,
        "3": buscar_produto,
        "4": executar_polimorfismo,
    }

    while True:
        exibir_menu()
        opcao = ler_texto("Escolha uma opção: ")
        if opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        acao = acoes.get(opcao)
        if acao is None:
            print("Opção inválida. Tente novamente.")
        else:
            acao(lanchonete)


if __name__ == "__main__":
    main()

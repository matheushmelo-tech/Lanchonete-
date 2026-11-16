"""Programa principal da lanchonete (delivery): menu interativo no terminal."""

from bebida import Bebida
from lanche import Lanche
from produto import Produto
from sobremesa import Sobremesa


class Lanchonete:
    """Classe gerenciadora que guarda a lista de produtos da lanchonete.

    A lista pode conter objetos de tipos diferentes (Lanche, Bebida,
    Sobremesa), todos filhos de Produto.
    """

    def __init__(self, nome="Lanchonete"):
        """Inicializa a lanchonete com uma lista de produtos vazia.

        Args:
            nome (str): nome da lanchonete (não pode ser vazio).

        Raises:
            ValueError: se o nome for vazio.
        """
        self.nome = nome
        self.__produtos = []

    @property
    def nome(self):
        """str: retorna o nome da lanchonete."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome da lanchonete, impedindo valores vazios.

        Raises:
            ValueError: se o nome for vazio ou conter apenas espaços.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome da lanchonete não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def produtos(self):
        """list: retorna uma cópia da lista de produtos cadastrados."""
        return self.__produtos.copy()

    def adicionar_produto(self, produto):
        """Cadastra um produto na lanchonete.

        Args:
            produto (Produto): objeto Produto (ou de uma classe filha).

        Raises:
            TypeError: se o objeto não for um Produto.
        """
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível cadastrar objetos do tipo Produto.")
        self.__produtos.append(produto)

    def buscar_por_nome(self, termo):
        """Busca produtos cujo nome contenha o termo informado.

        A busca ignora diferença entre maiúsculas e minúsculas.

        Args:
            termo (str): texto a ser procurado no nome dos produtos.

        Returns:
            list: lista com os produtos encontrados (pode ser vazia).
        """
        termo = termo.strip().lower()
        return [p for p in self.__produtos if termo in p.nome.lower()]

    def __len__(self):
        """Retorna a quantidade de produtos cadastrados."""
        return len(self.__produtos)

    def __str__(self):
        """Retorna um resumo da lanchonete de forma legível."""
        return f"Lanchonete: {self.__nome} | Produtos cadastrados: {len(self.__produtos)}"


def ler_texto(mensagem):
    """Lê um texto digitado pelo usuário.

    Args:
        mensagem (str): texto exibido ao usuário.

    Returns:
        str: texto digitado, sem espaços nas pontas.
    """
    return input(mensagem).strip()


def ler_numero(mensagem):
    """Lê um número digitado pelo usuário (aceita vírgula como decimal).

    Repete a pergunta até que um número válido seja informado.

    Args:
        mensagem (str): texto exibido ao usuário.

    Returns:
        float: número digitado.
    """
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex: 12.50).")


def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n===== LANCHONETE DELIVERY =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto por nome")
    print("4 - Calcular preço final (polimorfismo)")
    print("0 - Sair")


def criar_lanche():
    """Pede os dados ao usuário e cria um Lanche.

    Returns:
        Lanche: objeto criado.
    """
    nome = ler_texto("Nome do lanche: ")
    preco = ler_numero("Preço (R$): ")
    pao = ler_texto("Tipo de pão: ")
    texto = ler_texto("Ingredientes (separados por vírgula, opcional): ")
    ingredientes = [i.strip() for i in texto.split(",") if i.strip()]
    return Lanche(nome, preco, pao, ingredientes)


def criar_bebida():
    """Pede os dados ao usuário e cria uma Bebida.

    Returns:
        Bebida: objeto criado.
    """
    nome = ler_texto("Nome da bebida: ")
    preco = ler_numero("Preço base (R$): ")
    tamanho_ml = ler_numero("Tamanho (ml): ")
    gelada = ler_texto("É gelada? (s/n): ").lower() == "s"
    return Bebida(nome, preco, tamanho_ml, gelada)


def criar_sobremesa():
    """Pede os dados ao usuário e cria uma Sobremesa.

    Returns:
        Sobremesa: objeto criado.
    """
    nome = ler_texto("Nome da sobremesa: ")
    preco = ler_numero("Preço (R$): ")
    sabor = ler_texto("Sabor: ")
    return Sobremesa(nome, preco, sabor)


def cadastrar_produto(lanchonete):
    """Opção 1: cadastra um novo produto na lanchonete.

    Args:
        lanchonete (Lanchonete): lanchonete que receberá o produto.
    """
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
    """Opção 2: lista todos os produtos cadastrados.

    Args:
        lanchonete (Lanchonete): lanchonete a ser listada.
    """
    print(f"\n--- {lanchonete} ---")
    if len(lanchonete) == 0:
        print("Nenhum produto cadastrado.")
        return
    for numero, produto in enumerate(lanchonete.produtos, start=1):
        print(f"{numero}. {produto}")


def buscar_produto(lanchonete):
    """Opção 3: busca produtos pelo nome.

    Args:
        lanchonete (Lanchonete): lanchonete onde a busca será feita.
    """
    termo = ler_texto("\nNome (ou parte do nome) a buscar: ")
    encontrados = lanchonete.buscar_por_nome(termo)
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
    print(f"\n{len(encontrados)} produto(s) encontrado(s):")
    for produto in encontrados:
        print(f"- {produto}")


def executar_polimorfismo(lanchonete):
    """Opção 4: chama calcular_preco_final() em todos os produtos.

    Percorre a lista com objetos de tipos diferentes e chama o mesmo
    método em todos, mostrando que cada tipo responde de um jeito.

    Args:
        lanchonete (Lanchonete): lanchonete com os produtos.
    """
    if len(lanchonete) == 0:
        print("\nNenhum produto cadastrado.")
        return
    print("\n--- Preço final de cada produto ---")
    for produto in lanchonete.produtos:
        tipo = type(produto).__name__
        print(f"[{tipo}] {produto.nome}: R$ {produto.calcular_preco_final():.2f}")


def main():
    """Executa o menu até o usuário escolher a opção de sair."""
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
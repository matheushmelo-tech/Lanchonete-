"""Módulo contendo a classe Lanche, especializada de Produto."""
import Produto


class Lanche(Produto):


"""Representa um lanche/sanduíche no sistema de delivery.
    Herda da classe base Produto e adiciona atributos e métodos específicos
    para a montagem e personalização de lanches.
    """


def __init__(self, nome: str, preco: float, pao: str, ingredientes: list[str] | None = None) -> None:


"""Inicializa um novo Lanche.
        :param
 nome: Nome comercial do lanche.
        :param
 preco: Preço em reais (R$).
        :param
 pao: Tipo de pão utilizado (ex: 'Brioche', 'Australiano').
        :param
 ingredientes: Lista inicial de ingredientes do lanche.
        """
super().__init__(nome, preco)
self.pao = pao
# Executa o setter da propriedade pao (com validação)
self._ingredientes: list[str] = ingredientes if ingredientes is not None else []


@property
def pao(self) -> str:


"""Obtém o tipo de pão do lanche.
        :return
: Nome/tipo do pão.
        """
return self._pao


@pao.setter
def pao(self, valor: str) -> None:


"""Define e valida o tipo de pão.
        :param
 valor: Nome do pão informado.
        :raises
 ValueError: Caso o texto seja vazio ou apenas espaços.
        """
if not isinstance(valor, str) or not valor.strip():
    raise ValueError("O tipo de pão não pode ser vazio.")
self._pao = valor.strip()


@property
def ingredientes(self) -> list[str]:


"""Obtém a lista de ingredientes do lanche.
        :return
: Uma cópia da lista de ingredientes.
        """
return self._ingredientes.copy()


def adicionar_ingrediente(self, ingrediente: str) -> None:
    """Método próprio da classe Lanche.


    Permite personalizar o lanche adicionando novos ingredientes à receita.
    :param
ingrediente: Nome do ingrediente a ser inserido.
    :raises
ValueError: Se o nome do ingrediente for inválido.
    """
    if not isinstance(ingrediente, str) or not ingrediente.strip():
        raise ValueError("O nome do ingrediente deve ser válido.")

    item = ingrediente.strip()
    self._ingredientes.append(item)
    print(f"Ingrediente '{item}' adicionado ao lanche '{self.nome}'.")


def preparar(self) -> str:
    """Sobrescreve o mé
todo polimórfico da classe base Produto.
    :return
: Descrição detalhada da etapa de preparo do lanche na cozinha.
    """
    ingredientes_str = ", ".join(self._ingredientes) if self._ingredientes else


"sem recheio adicional"
return (
    f"[COZINHA - LANCHE] Selando pão {self._pao}
    , grelhando o hambúrguer "
f"e montando os ingredientes: {ingredientes_str}
."
)


def __str__(self) -> str:


"""Retorna a representação legível em texto do objeto Lanche.
        :return
: String com dados do lanche formatados.
        """
ingredientes_fmt = ", ".join(self._ingredientes) if self._ingredientes else
"Receita padrão"
return (
        f"Lanche: {self.nome} | Preço: R$ {self.preco:.2f}
        | "
          f"Pão: {self._pao} | Ingredientes: {ingredientes_fmt}
          "
)
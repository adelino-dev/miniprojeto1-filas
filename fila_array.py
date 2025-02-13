# Baseado em código do livro:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Gdados_antigoswasser
#    John Wiley & Sons, 2013
#
# License <http://www.gnu.org/licenses/>.


class FilaVazia(Exception):
    pass

class FilaArray:
    CAPACIDADE_PADRAO = 5
    
    def __init__(self):
        self._dados = [None]*FilaArray.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0
    
    def __len__(self):
        return self._tamanho
    
    def is_empty(self):
        return self._tamanho == 0
    
    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) %len(self._dados)
        self._tamanho -= 1
        return result
    
    def enqueue(self, e):
        if self._tamanho == len(self._dados):
            self._aumenta_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1
    
    def _aumenta_tamanho(self, novo_tamanho):
        dados_antigos = self._dados # keep track of existing list
        self._dados = [None] * novo_tamanho # allocate list with new capacity
        posicao = self._inicio
        for k in range(self._tamanho): # only consider existing elements
            self._dados[k] = dados_antigos[posicao] # intentionally shift indices
            posicao = (1 + posicao) %len(dados_antigos) # use dados_antigos size as modulus
        self._inicio = 0 # front has been realigned
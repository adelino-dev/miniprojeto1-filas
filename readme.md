# Mini Projeto 1 - Implementação de um Conjunto Usando Fila

Este repositório contém a implementação do primeiro mini projeto da disciplina de Estruturas de Dados 2024.1. O objetivo deste projeto é desenvolver uma estrutura de dados do tipo conjunto (set) utilizando uma fila, garantindo a não duplicidade de elementos.

## Descrição do Projeto

### Objetivos
- Implementar um tipo `SetWithQueue` que utiliza uma fila (`Fila_Array`) para armazenar elementos.
- As operações obrigatórias a serem implementadas são:
  - **add(element)**: Adiciona um elemento ao conjunto. Se o elemento já existir, não deve ser adicionado novamente.
  - **remove(element)**: Remove um elemento do conjunto. Se o elemento não existir, deve lançar uma exceção.
  - **contains(element)**: Retorna `True` se o elemento estiver no conjunto; caso contrário, retorna `False`.
  - **size()**: Retorna o número de elementos no conjunto.
  - **list()**: Retorna todos os elementos do conjunto.

### Discussão sobre Desempenho
O projeto inclui uma discussão sobre o desempenho de cada uma das operações desenvolvidas, que pode ser encontrada no arquivo `leiame.txt` (ou `readme.txt`).

## Realização e Entrega

- **Período de Entrega**: De 07/10 até 14/10.
- **Formato**: O projeto pode ser realizado individualmente ou em equipes de até 3 pessoas.
- **Entrega**: 
  - Arquivos do código-fonte ou um link (GitHub ou Replit).
  - Um arquivo `leiame.txt` contendo:
    - Integrantes da equipe.
    - Lista de todo o conteúdo consultado para a realização do projeto (sites, livros, artigos, códigos prontos, etc.).
    - Comentário da equipe sobre a execução das propostas.
    - Comentários sobre problemas identificados no código, dificuldades enfrentadas e funcionalidades não implementadas.

### Critérios de Avaliação
1. O projeto deve ser executado sem erros.
2. Deve utilizar a implementação de `Fila_Array` como base para implementar o tipo `SetWithQueue`.
3. A especificação solicitada deve ser realizada.
4. O código deve passar no conjunto de testes apresentados.
5. Deve haver um comentário sobre o desempenho das operações desenvolvidas.
6. Indicar qualquer material consultado (códigos, livros, sites, etc.) na realização do trabalho.
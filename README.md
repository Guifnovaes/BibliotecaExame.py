# Sistema de Controle de Biblioteca (CLI)

## Apresentação:

Para o nosso projeto foi escolhido um sistema de gerenciamento de biblioteca com as seguintes funções:

- Cadastrar livros  
- Cadastrar usuários  
- Realizar empréstimos  
- Visualizar a lista de livros e empréstimos  
- Acompanhar um log de operações realizadas  

Nosso sistema utilizou seis estruturas de dados

------------------------------

## Pré-requisitos para execução:

- Python instalado

## Como executar:

1. Salve o arquivo com o nome `sistema_biblioteca.py`.  
2. No terminal, execute o projeto com `python sistema_biblioteca.py`.  
3. Utilize o menu interativo para selecionar as opções.

---------------------

## Funções

- **Cadastrar livros:** informa título e autor.  
- **Cadastrar usuários:** informar nome e CPF do usuário.  
- **Realizar empréstimos:** relaciona um livro a um usuário no sistema.  
- **Listar livros e empréstimos:** lista todos os registros cadastrados.  
- **Ver log de operações:** mostra todo o histórico do sistema (cadastros e empréstimos).  
- **Registrar e visualizar histórico de devoluções:** acompanha as devoluções realizadas.

--------------------------------------

## Estruturas de Dados Utilizadas no sistema:

O projeto foi construído utilizando sete estruturas de dados:

1. **Listas**  
   - Onde: Armazenamento de livros e empréstimos.  
   - Por quê: Permite ordenação e iteração simplificada para registrar dinamicamente.

2. **Tuplas**  
   - Onde: Cada entrada no log de operações é uma tupla (tipo, descrição).  
   - Por quê: Tuplas são imutáveis e ocupam pouco espaço, excelentes para registros permanentes.

3. **Conjuntos**  
   - Onde: `livros_set` armazena os nomes dos livros.  
   - Por quê: Impede duplicação de títulos.

4. **Dicionários**  
   - Onde: Mapeia CPFs aos usuários.  
   - Por quê: Permite acesso rápido e direto a dados com base em uma chave única.

5. **Lista Encadeada**  
   - Onde: `log_operacoes` para registro sequencial das operações do sistema.  
   - Por quê: Demonstra manipulação de nós encadeados, útil em contextos com inserção constante e visualização sequencial.

6. **Lista Duplamente Encadeada**  
   - Onde: `historico_devolucoes` para registrar o histórico de devoluções de livros.  
   - Por quê: Permite navegação bidirecional nos registros, facilitando consultas mais flexíveis e a manipulação eficiente do histórico de devoluções.

7. **Classes**  
   - Classes: `Livro`, `Usuario` e `Emprestimo` para encapsulamento de dados relacionados.

---

## Finalização:

Nosso projeto apresenta como múltiplas estruturas de dados podem ser integradas em um sistema real e útil, com boa legibilidade e fácil manutenção.  

Cada funcionalidade foi pensada para representar situações reais de uma biblioteca e para demonstrar a prática dos conceitos das estruturas utilizadas.

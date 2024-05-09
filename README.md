# max-people-test

## Rodando  a aplicação

  - Clone o repositório seguindo o comando abaixo:
```bash
# Clonar repositório direto do git
git clone https://github.com/gabeoliva/max-people-test.git
``` 
  - Abra a pasta dentro do Visual Studio Code.
  - Certifique-se de ter o Python 3 instalado em seu computador.
  - Em seguida, no terminal do vscode, digite o seguinte comando:
```bash
# Windows:
python main.py
```
```bash
# Linux:
python3 main.py
```

## Descrição Geral

Este é um projeto cujo **objetivo** era o de suprir a necessidade de um cliente em obter a quantidade de passageiros, simultaneamente dentro de um determinado espaço físico, a partir de dados como horário de entrada e horário de saída dos mesmos. Ele oferece um caminho rápido e dinâmico para o alcance desses resultados.


## Principais Recursos

- Dados pré-definidos
- Visualização rápida e de fácil entendimento dos resultados


## Descrição Técnica

O projeto foi desenvolvido na linguagem de programação *Python*, e foi estruturado para ser simples e objetivo, da seguinte forma:

Foi criada a **função** *get_max_people*. Essa função recebe como parametro os seguintes elementos: **N**, **E** e **S**. Onde N é a quantidade de passageiros, E é o horário de entrada de cada passageiro e S o horário de saída.

Dentro da função citada acima, foi passada uma lista vazia, inicialmente, nomeada de *max_people*.
Em seguida, foram realizadas as seguintes **condições**:

  - O primeiro *if* verifica se pelo menos uma das variáveis **E** ou **S** é falsa. Se uma delas for falsa (ou ambas), o bloco de código indentado sob o if será executado.
  - Já no segundo *if*, verifica se **N** está fora do intervalo de 1 a 100. Se N estiver fora deste intervalo, o bloco de código indentado será executado, e a instrução return 0 fará   
    com que a função retorne o valor 0. Se N estiver dentro do intervalo de 1 a 100, o bloco de código indentado não será executado e a função continuará sua execução além desse bloco 
    condicional.

Após verificarmos essas condições, o código prossegue e percorre N. 
Em *entry_1*, é obtido o índice 0 da lista E, assim como em *exit_1*, porém, em *exit_1* será da lista S, e como resultado dos dois índices das respectivas listas, a saída será (1,9).
Já na variável *people_in_room = 1*, captamos a quantidade inicial de pessoas na sala, que nesse caso, foi **pré-definido** como 1. 

Sendo assim, foi criado um segundo *for*, visando evitar a repetição do elemento (neste caso, o horário) anterior através da declaração *i+1*.
No terceiro e último *if*, a lógica utilizada foi: se ambas as condições forem verdadeiras, significa que uma pessoa entrou na sala. Essa linha de código conta o número de pessoas que estão na sala, durante esse período de tempo específico.

**Finalizando:**
  *max_people.append(people_in_room)* - adiciona o número atual de pessoas na sala à lista *max_people*, citada no começo deste tópico (a **lista vazia**).
  *return max(max_people)* - retorna o maior valor contido na lista *max_people*, que representa o maior número de pessoas (passageiros) na sala em qualquer momento, durante o período    
  declarado.

  Por fim, fora da função, temos as váriaveis N, E e S, explicadas acima, e a função print, usada para calcular e imprimir o resultado retornado pela função get_max_people(N, E, S).

  













   

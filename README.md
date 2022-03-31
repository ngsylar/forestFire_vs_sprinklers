# forest_fire_vs_sprinklers
Experimento da tarefa 5.2 de Computação Experimental 2021/2

    Gabriel Rocha Fontenele
    Matrícula: 15/0126760

# Modelo
O modelo escolhido consiste no modelo de exemplo para o framework MESA padrão referente a simulação forest_fire. A modificação feita nesta tarefa consiste em manipular a densidade de um novo tipo de agente presente na floresta: os sprinkler.

## Hipótese levantada: 
Aumentando-se a quantidade de sprinklers instalados em uma floresta, maior será o tamanho médio de áreas florestais preservadas após uma queimada.

## Alterações e justificativas:

***server.py:***
Foi adicionado o parâmetro manipulável de densidade de sprinklers. Assim, é possível que o usuário controle a quantidade de agentes inibidores que atuarão durante a simulação. O parâmetro pode ser modificado mediante a interface web. As árvores salvas pelos sprinklers assumem a cor azul, através de uma chave que foi adicionada às cores que representam os estados das árvores na grade de ocupação.

***model.py:***
No modelo, durante a criação dos agentes do tipo árvore, as ávores próximas aos sprinklers tem dispersão de 1 célula para as diagonais e alcance de até 8 células à direita de um sprinkler. As árvores compreendidas nessa área possuem maior probalidade de não serem afetadas pelo fogo. A probabilidade distribuída de que uma árvore, a partir do agente inibidor até a última árvore compreendida pelo alcance, pegue fogo vai de 8% a 98%, a medida que vai se afastando para a direita. Quanto maior for a quantidade e dispersão dos sprinklers, maior será o alcance de árvores que eles conseguem salvar do fogo.

***agent.py:***
Durante uma queimada, a medida que o fogo se aproxima de uma árvore próxima a um sprinkler, a intensidade do fogo é atribuída através de uma variável randômica, que pode ultrapassar ou não a resistência ao fogo que a árvore possui. Quando mais próxima de um sprinkler ela estiver, menor será a chance de que ela seja queimada. A variável que representa essa probabilidade foi chamada de strength no código.

## Como usar o simulador:
A partir do diretório raiz do framework mesa, rode o comando

    mesa runserver <caminho da pasta>/forest_fire_vs_sprinklers

A partir da interface web, pode se modificar os valores das densidades, tanto das ávores quanto dos bombeiros, através dos seus respectivos sliders, com clique e arraste. Quando maior for o valor de cada densidade, maior será o número de agentes presentes na grade de ocupação e consequentemente participantes da simulação após o início da simulação.

A simulação acaba quando não houver mais fogo atuando na simulação ou se interrompida pelo usuário através do botão de parada.

## Coleta de dados:
Após o fim de uma simulação, dois arquivos de extensão .csv são gerados, cada um contendo dados relevantes referentes a observação do experimento, sendo eles:

***agent_data:*** contendo valores assumidos pelas variáveis a nível de agente durante toda a execução da simulação, em forma de tabela, onde cada coluna apresnta os resultados para:
* a iteração e funciona como se fosse o decorrer do tempo durante a observação de um fenômeno real.
* a quantidade de árvores que até a enésima iteração não foram afetadas pela propagação do fogo.
* a quantidade de árvores nas quais o fogo foi rapidamente apagado, evitando a propagação do incêndio, até a enésima iteração.
* a quantidade de árvores danificadas pelo fogo.
* a quantidade de árvores em chamas. 

***model_data:*** esse arquivo apresenta, as colunas com o valor dos parâmetros escolhido pelo usuário, sendo eles o tamanho da floresta em posições quadradas, a densidade das árvores e a densidade de sprinklers. As demais colunas mostram no final da simulação os seguintes resultados:
* o tamanho médio dos agrupamentos de árvores saudáveis;
* a quantidade de agrupamentos de árvores saudáveis na floresta;
* a soma das quantidades de árvores não afetadas pelas chamas e de árvores não afetadas pelo fogo em razão do total de árvores na floresta;
* a quantidade de árvores cujo fogo foi rapidamente apagado pela ação dos sprinklers em razão do total de árvores na floresta;
* e por fim a quantidade de vegetação queimada em razão do total de árvores na floresta;

fornecendo assim uma idéia geral sobre a eficácia da ação dos agentes inibidores.

# Forest Fire Model (Descrição do Modelo Original do Framework MESA)

## Summary

The [forest fire model](http://en.wikipedia.org/wiki/Forest-fire_model) is a simple, cellular automaton simulation of a fire spreading through a forest. The forest is a grid of cells, each of which can either be empty or contain a tree. Trees can be unburned, on fire, or burned. The fire spreads from every on-fire tree to unburned neighbors; the on-fire tree then becomes burned. This continues until the fire dies out.

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

To view and run the model analyses, use the ``Forest Fire Model`` Notebook.

## Files

### ``forest_fire/model.py``

This defines the model. There is one agent class, **TreeCell**. Each TreeCell object which has (x, y) coordinates on the grid, and its condition is *Fine* by default. Every step, if the tree's condition is *On Fire*, it spreads the fire to any *Fine* trees in its [Von Neumann neighborhood](http://en.wikipedia.org/wiki/Von_Neumann_neighborhood) before changing its own condition to *Burned Out*.

The **ForestFire** class is the model container. It is instantiated with width and height parameters which define the grid size, and density, which is the probability of any given cell having a tree in it. When a new model is instantiated, cells are randomly filled with trees with probability equal to density. All the trees in the left-hand column (x=0) are set to *On Fire*.

Each step of the model, trees are activated in random order, spreading the fire and burning out. This continues until there are no more trees on fire -- the fire has completely burned out.


### ``forest_fire/server.py``

This code defines and launches the in-browser visualization for the ForestFire model. It includes the **forest_fire_draw** method, which takes a TreeCell object as an argument and turns it into a portrayal to be drawn in the browser. Each tree is drawn as a rectangle filling the entire cell, with a color based on its condition. *Fine* trees are green, *On Fire* trees red, and *Burned Out* trees are black.

## Further Reading

Read about the Forest Fire model on Wikipedia: http://en.wikipedia.org/wiki/Forest-fire_model

This is directly based on the comparable NetLogo model:

Wilensky, U. (1997). NetLogo Fire model. http://ccl.northwestern.edu/netlogo/models/Fire. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

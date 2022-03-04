# forest_fire_vs_fireman
Experimento da tarefa 5.2 de Computação Experimental 2021/2

    Gabriel Rocha Fontenele
    Matrícula: 15/0126760

# Modelo
O modelo escolhido consiste no modelo de exemplo para o framework MESA padrão referente a simulação forest_fire. A modificação feita nesta tarefa consiste em manipular a densidade de um novo tipo de agente presente na floresta: o bombeiro.

A adição foi pensada para responder a seguinte pergunta: "o que acontece se houver um agente inibidor do fenômeno fogo?"

## Hipótese levantada: 
Aumentando-se a densidade de agentes inibidores de fogo, bombeiros, consequentemente maior será a quantidade desse tipo de agente presente na floresta e maior a probabilidade de o fogo cessar ou pelo menos reduzir os danos causados à vegetação por uma queimada.

## Alterações e justificativas:

server.py: 
Foi adicionado o parâmetro manipulável de densidade de bombeiros. Assim, é possível que o usuário controle a quantidade de agentes bombeiros que atuarão durante a simulação. O parâmetro pode ser modificado mediante a interface web. Um pequeno ponto de cor azul foi adicionado à grade de ocupação para indicar a posição em que um agente bombeiro se encontra.

model.py: 
No modelo, durante a criação dos agentes do tipo árvore, as ávores à direita dos bombeiros tem dispersão de 1 célula para as diagonais e alcance de até 8 células à direito de um bombeiro. As árvores compreendidas nessa área possuem maior probalidade de não serem afetadas pelo fogo. A probabilidade distribuída de que uma árvore, a partir do agente inibidor até a última árvore compreendida pelo alcance, pegue fogo vai de 2%, 6%, 14%, 30% até 60% a medida que vai se afastando para a direita.

agent.py
Durante uma queimada, a medida que o fogo de aproxima de uma árvore próxima a um bombeiro, a intensidade do fogo é atribuída através de uma variável randômica, que pode ultrapassar ou não a resistência que árvora apresenta. Quando mais próxima do bombeiro ela estiver, porém, menor será a chance de que ela seja atingida pelo fogo. A variável que representa essa probabilidade, foi chamado de strength no código.

## Como usar o simulador:
A partir da interface web, pode se modificar os valores das densidades, tanto das ávores quanto dos bombeiros, através dos seus respectivos sliders, com clique e arraste. Quando maior for o valor de cada densidade, maior será o número de agentes presentes na grade de ocupação e consequentemente participantes da simulação após o início da simulação.

A simulação acaba quando não houver mais fogo atuando na simulação ou se interrompida pelo usuário através do botão de parada.

## Coleta de dados:
Após o fim de uma simulação, dois arquivos de extensão .csv são gerados, cada um contendo dados relevantes referentes a observação do experimento, sendo eles:

agent_data: contendo valores assumidos pelas variáveis a nível de agente durante toda a execução da simulação, em forma de tabela. A primeira coluna mostra a iteração e funciona como se fosse o decorrer do tempo durante a observação de um fenômeno real. A segunda coluna mostra a quantidade de árvores que até a enésima iteração não foram afetadas pela propagação do fogo. A terceira coluna mostra a quantidade de árvores em chamas e a quarta representa a quantidade de árvores danificadas pelo fogo.

A quinta coluna fornece informação sobre a quantidade de bombeiros presentes no combate ao fogo. O valor assumido por essa variável recebe influência direta do valor de densidade de bombeiros, escolhido pelo usuário, embora o número permaneça fixo até o final da simulação.

model_data: esse arquivo apresenta as densidades escolhidas pelo usuário para uma simulação e mostra a quantidade de árvores afetadas e árvores não afetadas pelo formo em termos de porcentagem, fornecendo assim uma idéia geral sobre a eficácia da ação dos agentes inibidores, chamados de bombeiros.

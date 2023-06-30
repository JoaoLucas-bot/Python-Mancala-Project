Relatório

Pretendemos com este relatório fazer um “overview” do nosso projeto, de forma a que fique mais clara a nossa “linha de pensamento” relativamente ao seu desenvolvimento.

Este projeto foi elaborado pelos seguintes alunos: Luís Dias (30009279), João Lucas (30008215), Pedro Amaral (30008241) e Eduardo Araújo (30008290).

No desenvolvimento de todo o código, o mesmo foi feito de forma remota, em que um dos elementos do grupo partilhava a tela do computador e todos os outros iam contribuindo para o pensamento e construção do código.
Todo o conceito, bem como a aplicação do mesmo foi desenvolvido em Python, na versão 3.10, através da “tool” Visual Studio Code e com recurso ao modelo “MVC”. 
Utilizámos o ficheiro “view.py” para escrever todo o código, relativo à interação com o utilizador. O “program.py” foi utilizado para a execução do código e o “controller.py” tem todas as funções de manipulação e armazenamento de dados. Por fim, o “model.py” não foi utilizado para este projeto.

Tivemos necessidade de importar um módulo externo, denominado “pickle”, que faz parte da biblioteca “python” e que se utilizou para arquivar e ler o estado do jogo dentro dum ficheiro. 
Desenvolveu-se um programa que tem como finalidade a execução do jogo “Mancala”, tendo em conta todas as regras pedidas no enunciado “README.md”. 

Como principais decisões e linhas de raciocínio, gostaríamos de destacar a função “iniciar”, que tem no dicionário “jogo” toda a estrutura fundamental do jogo e respetivo armazenamento. 





Assim as principais linhas de raciocino foram:

- tabela_resultados: Decidimos utilizar o método de “dicionários” para o armazenamento de dados relativamente a número de jogos, vitórias, empates e derrotas dos respetivos jogadores. Isto porque, entendemos que seria mais percetível, organizado e menos suscetível a “erros”, tornando-se uma solução bastante eficiente.

- controlador_jogo: O valor desta chave é “booleano”, de forma a utilizá-lo no código como forma de controlo.

- jogadores_em_jogo: Utilizámos uma lista para sabermos a qualquer momento, quais os jogadores que se encontravam em jogo. A escolha pela lista tem também em consideração o fácil acesso à mesma, tendo em conta o  uso de “indexes”.

- tabuleiro_jogo: Inicialmente, usámos o “tabuleiro_jogo” como um dicionário, onde a chave era o “nome do jogador” e o valor era uma lista com os respetivos buracos e poço. No entanto, verificámos que esta opção não seria prática nesta situação, de modo que preferimos utilizar apenas uma lista de modo a armazenar o tabuleiro de jogo.  

- modo_jogo: Sobre esta chave, cujo valor é uma “string”, o objetivo é guardar o “modo de jogo” selecionado pelo utilizador no comando “IJA”.

Por fim, não nos “desenvolvemos” muito relativamente à descrição do código do projeto, tendo em conta que este se encontra todo comentado no código.



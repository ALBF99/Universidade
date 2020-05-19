# Introdução

* Este trabalho foi realizado a pedido dos professores Pedro Salgueiro e Mário Mourão de  Metodologias e Desenvolvimento de Software, e tem como objectivo a criação e implementação por parte dos alunos de um sistema de marcação de férias, bem como os seus testes, recorrendo à matéria leccionada, aos use cases que foram descritos pelos professores e o diagrama de classes desenvolvido na primeira parte do trabalho.

# Descrição do Sistema de Marcação de Férias

Pretende-se desenvolver um sistema de gestão de férias numa empresa que permita aos colaboradores da empresa fazerem a marcação das suas férias e aos gestores fazerem a gestão das férias de todos os colaboradores. 

Os requisitos do sistema especificados pelo cliente estão descritos nos seguintes parágrafos:

* Os colaboradores podem usar o sistema para submeter, consultar ou cancelar os seus pedidos de férias.  Os pedidos submetidos devem ser aprovados ou rejeitados pelo gestor.

* Os recursos humanos devem poder consultar todos os pedidos de férias efectuados. Bem como o nº de dias de férias atribuídos a cada colaborador.

O sistema deve ter em conta as seguintes regras:

*  Cada colaborador tem direito a gozar os dias de férias estipulados pelo Código de Trabalho em Vigor (22 dias úteis).

*  Por cada 5 anos de antiguidade cada colaborador tem direito a um dia adicional de férias até um máximo de 5 dias úteis.

*  85% dos dias de férias têm que ser marcadas até 31 Março do ano actual.

*  Pelo menos um dos períodos de férias deve ser de duas semanas. Nos meses de Junho a Setembro não deve ser marcado mais do que um período de duas semana de forma a não penalizar os restantes colaboradores.

*  As férias relativas ao ano anterior ainda não gozadas devem ser gozadas até ao dia 20 de Junho.

*  O colaborador pode solicitar que um período de férias seja cancelado, voltando a ter disponíveis os dias para remarcar.

*  Cada colaborador tem uma pontuação, consoante as férias que gozou no ano anterior e aplicando a fórmula : nº de dias de férias a multiplicar pela pontuação do respectivo mês (ver Tabela 1). Esta pontuação deve ser usada pela aplicação para indicar ao gestor quem tem prioridade quando dois ou mais colaboradores façam pedidos de férias para períodos sobrepostos e não possam tirar férias simultaneamente. Numa situação destas, deve ser escolhido o  colaborador que tem menor pontuação. O sistema apenas disponibiliza esta informação para ao gestor, não devendo decidir automaticamente por ele.


Tabela 1: Pontos por cada dia de férias

| Meses | Pontos por cada dia de Férias |
| ------ | ------ |
| Janeiro, Fevereiro e Novembro | 1 |
| Março, Abril, Maio e Outubro | 2 | 
| Junho e Setembro | 3 |
| Julho, Agosto e Dezembro | 4 | 

Para a segunda parte do trabalho, algumas especificações acima ficaram de parte. São elas:

* Os recursos humanos devem poder consultar todos os pedidos de férias efectuados. Bem como o nº de dias de férias atribuídos a cada colaborador.

* Por cada 5 anos de antiguidade cada colaborador tem direito a um dia adicional de férias até um máximo de 5 dias úteis.

* 85% dos dias de férias têm que ser marcadas até 31 Março do ano atual.

* As férias relativas ao ano anterior ainda não gozadas devem ser gozadas até ao dia 20 de Junho.

* O colaborador pode solicitar que um período de férias seja cancelado, voltando a ter disponíveis os dias para remarcar.

* Pelo menos um dos períodos de férias deve ser de duas semanas. Nos meses de Junho a Setembro não deve ser marcado mais do que um período de duas semana de forma a não penalizar os restantes colaboradores.


# Descrição do trabalho

* Para a implementação do Sistema de Marcação de Férias em linguagem Java, decidimos que para guardar tanto os utilizadores, bem como os seus pedidos e bem como os pedidos de todos os utilizadores, utilizar uma ArrayList.
* Para podermos diferenciar que cargo têm os utilizadores, definimos que quando ao introduzir um username seria do tipo "C-XXXX" ou "G-XXXX" de modo a poder fazer essa diferenças, porém não era uma opção ´viável. Assim, decidimos deixar na mesma essa carcterística para podermos "atualizar" o boolean que difere se é gestor(true) ou se é coloborador(false). Portanto, se o primeiro caracter for um "C" o boolean fica a false e se for um "G" o boolean passa a true, fazendo essa diferença, de modo a que depois só apareçam as opções definidas para cada um.
* Decidimos também interpretar que nenhum colaborador ou gestor trabalha ao fim de semana. Assim, e como o nome indica, os dias úteis serão só de segunda a sexta, e para podermos implementar essa estratégia, tivemos que aos dias escolhidos pelo utilizador retirar aqueles que correspondiam tanto ao sábado como ao domingo.
* Decidimos também que para as contas dos dias acima, os feriados não iriam ser contabilizados. 

# Conclusão

* Em suma, com este trabalho (quer a primeira parte quer a segunda parte), achamos que conseguimos adquirir várias competências, quer sobre os conceitos básicos de UML, quer sobre descrição e desenvolvimento de software, quer sobre os conceitos básicos do git, bem como os testes necessários para a implementação do sistema, que certamente serão úteis no futuro. Com vista na nossa interpretação, acreditamos que conseguimos atingir os objectivos com sucesso.
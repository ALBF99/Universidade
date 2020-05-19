	O objetivo desde programa é calcular a menor distancia entre dois pontos de familias diferentes. So pode haver duas familias, 0 e 1, no minimo deve haver dois pontos e no maximo 100 000. As coordenadas X e Y podem variar entre 0 e 1 000 000 000.
O input comeca com um inteiro N (Numero de pontos) e nas seguintes linhas tres inteiros: X,Y,F, que correspondem as coordenadas dos pontos e a sua familia.
O output deve ser um print da menor distancia entre dois pontos de diferentes familias.
Para isto criamos uma funcao matriz que nao recebe nada e le as linhas que esta no ficheiro input.txt e diviti-as em elementos para a lista a qual demos o nome de matriz, retorna a lista matriz em que cada elemento corresponde a cada elemento de uma linha em string, menos a ultima linha que e retirada da matriz.
A seguir foi criada a funcao dividir_familias recebe a lista matriz dividi-a em duas listas: uma com as coordenadas da familia 0 e outra com as coordenadas da familia 1, retorna as duas listas arr_F0 e arr_F1 com as coordenadas correspondentes a cada familia.
Depois criamos outra funcao to_int que recebe as listas arr_F0 e arr_F1 e passa cada elementos das duas listas para inteiros e retorna essas mesmas listas.
Por fim, criamos a funcao menor que recebe as listas arr_F0 e arr_F1 descobre a menor distancia entre dois elementos entre os dois arrays e retorna esse valor.
No final fizemos apenas um print do valor.


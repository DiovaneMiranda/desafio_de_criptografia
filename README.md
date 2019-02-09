# desafio_de_criptografia
A Prime scramble cryptography challenge

Desafio de criptografia:Desenvolver um algoritmo em qualquer linguagem de programação que tome como input uma string criptografada e a imprima descriptografada.
Criptografia Prime-Scramble:O valor ASCII de cada membro da string é somado ao número primo de mesmo índice. Exemplo:
#a b c d e f g h i j
#+ + + + + + + + + +
2 3 5 7 11 13 17 19 23 29
= = = = = = = = = =
c e h k p s x { # *
limite inferior: VALOR DECIMAL = 33 <=> CARACTERE = !
limite superior: VALOR DECIMAL = 125 <=> CARACTERE = }

Note que caso a soma do caractere com o número primo seja maior do que o limite superior, ele deve começar novamente a partir do limite inferior. Por exemplo:
i(105) + 23 = 128. 128 > 125. criptografia = 33 + (128 - 126) = 35 = #

listaNumeros = [1,2,3,4,5];
listaStrings = ["e", "f", "c", "d"];
listaMista   = [1, "a", 3.14, True];
print(listaNumeros);
# Imprimir [1, 2, 3, 4, 5]

print(listaStrings);
# Imprimir ['e', 'f', 'c', 'd']

print(listaMista);
# Imprimir [1, 'a', 3.14, True]

frutas = ["maça", "banana", "morango"];
frutas[1] = "laranja";

print(frutas[0])
# Imprimir primiera começa numero em zero para maça

print("Tamanho 1: ", len(frutas))
# Imprimir comprimemto de strings no arry é Tamanho 1:  3

frutas.append("Abacaxi");
print(frutas)
# Imprimir um novo adicionar 'abacaxi' é ['maça', 'laranja', 'morango', 'Abacaxi']

print("Tamanho 2: ",len(frutas))
# Imprimir comprimemto de strings, pois um adicionou string de abacaxi no arry é Tamanho 2:  4

listaNova = [1, ["a", "b"]];
print(listaNova[1][0]);
# Imprimir como escolhe numero 1 para encontrado a

lista1 = [1,2,3];
lista2 = [4,5,6];
listaConcatenada = lista1 + lista2;
print(listaConcatenada);
# Imprimir concatenada é [1, 2, 3, 4, 5, 6]

listaRepetida = [0] * 4;
print(listaRepetida);
# Imprimir multiplicacao para 0, é [0, 0, 0, 0]

letras  = ["a", "b", "c", "d"];
sublista = letras[1:4];
print(sublista);
# Imprimir colocou escolhindo as letras é ['b', 'c', 'd']

frutas = ["maça", "banana", "laranja"];
frutas.append("morango");
print(frutas);
# Imprimir um novo adicionar 'morango' é ['maça', 'banana', 'laranja', 'morango']

frutas.insert(1, "abacaxi");
print(frutas);
print();
# Imprimir numero 1 de lugar e um novo inserir 'abacaxi' é ['maça', 'abacaxi', 'banana', 'laranja', 'morango']

frutaRemovida = frutas.remove("banana");
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);
# Imprimir removeu 'banana' ['maça', 'abacaxi', 'morango']

frutas.sort();
print("Embaralhado: ", frutas);
# Imprimir Embaralhado:  ['abacaxi', 'maça', 'morango']
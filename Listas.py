
nova_lista = []
lista = [1,2,3,4,5,6] #criando lista
outra_lista = [10,11]
print(lista[2]) #imprimindo indice da lista
lista[2] = 10 #alterando valor do elemento
print(lista[2]) #imprime novo elemento
lista[2] = 3 #alterando valor do elemento
print(lista[2]) #imprime novo elemento
#adicionando novos elemtentos à lista
lista.append(7) 
lista.append(8)
lista.append(9)
lista.append(outra_lista)
#imprime todos os elemtentos da lista
for x in lista:
    print(x)

minha_lista = [1, 'a', 3.14]
minha_lista.append('novo elemento')
print(minha_lista)


for i in range(5):
    nova_lista.append(i)
print(nova_lista)
